"""Core word-list engine.

Given a target language and a topic-weight profile, produce:

  * mandatory  - the "glue" words (articles, pronouns, prepositions, ...) that
                 every learner needs. Never counted against the 1000.
  * core       - the personalised list of up to `core_size` content words,
                 ranked by a blend of raw corpus frequency and how well the
                 word matches the learner's profile.

Frequency data comes from `wordfreq` (OpenSubtitles + web + other corpora).
"""

from functools import lru_cache
from typing import Dict, List, Optional

from wordfreq import top_n_list, zipf_frequency

from .data.function_words import FUNCTION_WORD_GLOSS, FUNCTION_WORD_SET
from .data.topics import TOPIC_LABELS, WORD_GLOSS, WORD_TOPICS

SUPPORTED_LANGUAGES = {"es": "Spanish", "fr": "French"}

# How many words to pull from the frequency corpus as raw candidates.
CANDIDATE_POOL = 6000
# Strength of the personalisation. 0 => pure frequency order.
# With BOOST_FACTOR = 0.6 a word carrying the learner's full weight on one
# strong topic roughly doubles its score.
BOOST_FACTOR = 0.6
# Extra implicit weight given to a curated word from a topic the learner picked,
# so hand-picked vocabulary reliably beats generic filler of the same frequency.
CURATED_BONUS = 0.5
DEFAULT_CORE_SIZE = 1000


@lru_cache(maxsize=8)
def _candidates(language: str) -> tuple:
    return tuple(top_n_list(language, CANDIDATE_POOL))


def _is_wordlike(word: str) -> bool:
    if len(word) < 2:
        return False
    if not any(ch.isalpha() for ch in word):
        return False
    if any(ch.isdigit() for ch in word):
        return False
    return True


def _normalise_profile(profile: Dict[str, float]) -> Dict[str, float]:
    """Scale weights to 0..1 so BOOST_FACTOR behaves predictably."""
    if not profile:
        return {}
    top = max(profile.values())
    if top <= 0:
        return {}
    return {t: w / top for t, w in profile.items() if w > 0}


def build_wordlist(
    language: str,
    profile: Optional[Dict[str, float]] = None,
    core_size: int = DEFAULT_CORE_SIZE,
) -> dict:
    if language not in SUPPORTED_LANGUAGES:
        raise ValueError(f"Unsupported language: {language!r}")

    profile = _normalise_profile(profile or {})
    fn_set = FUNCTION_WORD_SET[language]
    fn_gloss = FUNCTION_WORD_GLOSS[language]
    word_topics = WORD_TOPICS[language]
    word_gloss = WORD_GLOSS[language]

    candidates = _candidates(language)
    rank = {w: i for i, w in enumerate(candidates)}
    pool_size = len(candidates)

    def freq_score(word: str) -> float:
        # 1.0 for the most frequent word, decaying toward 0.
        r = rank.get(word, pool_size)
        return 1.0 - (r / pool_size)

    def topic_boost(word: str, extra: float = 0.0) -> float:
        weight = sum(profile.get(t, 0.0) for t in word_topics.get(word, ()))
        return 1.0 + BOOST_FACTOR * (weight + extra)

    # --- mandatory list: function words, in frequency order ------------------
    mandatory_seen = set()
    mandatory: List[dict] = []
    for word in candidates:
        if word in fn_set and word not in mandatory_seen:
            mandatory_seen.add(word)
            mandatory.append({
                "word": word,
                "gloss": fn_gloss.get(word, ""),
                "zipf": round(zipf_frequency(word, language), 2),
            })
    # any curated function words the corpus didn't surface
    for word, gloss in fn_gloss.items():
        if word not in mandatory_seen:
            mandatory_seen.add(word)
            mandatory.append({
                "word": word, "gloss": gloss,
                "zipf": round(zipf_frequency(word, language), 2),
            })

    # --- scored content-word pool -----------------------------------------
    scores: Dict[str, float] = {}
    for word in candidates:
        if word in fn_set or not _is_wordlike(word):
            continue
        scores[word] = freq_score(word) * topic_boost(word)

    # inject curated topic words even if they fell outside the raw pool,
    # and make sure picked-topic vocabulary is competitive. A word from a topic
    # the learner picked gets a base-score floor so that genuinely useful but
    # lower-frequency vocabulary (e.g. "passport", "pharmacy") can still land in
    # the list; words from topics they did not pick keep their raw frequency.
    picked_floor = 1.0 - (0.8 * core_size) / pool_size
    for word, topics in word_topics.items():
        if word in fn_set or not _is_wordlike(word):
            continue
        picked = any(profile.get(t, 0.0) > 0 for t in topics)
        base = freq_score(word)
        if picked:
            base = max(base, picked_floor)
        injected = base * topic_boost(word, extra=CURATED_BONUS if picked else 0.0)
        scores[word] = max(scores.get(word, 0.0), injected)

    ranked = sorted(scores, key=lambda w: scores[w], reverse=True)[:core_size]

    core: List[dict] = []
    for i, word in enumerate(ranked, start=1):
        topics = sorted(word_topics.get(word, ()))
        core.append({
            "rank": i,
            "word": word,
            "gloss": word_gloss.get(word, ""),
            "topics": topics,
            "topic_labels": [TOPIC_LABELS[t] for t in topics],
            "zipf": round(zipf_frequency(word, language), 2),
        })

    covered = sorted(
        {t for w in ranked for t in word_topics.get(w, ())},
        key=lambda t: TOPIC_LABELS[t],
    )
    # the topics the learner's answers actually steered toward, strongest first
    focus = sorted(profile, key=lambda t: profile[t], reverse=True)

    return {
        "language": language,
        "language_name": SUPPORTED_LANGUAGES[language],
        "core_size": len(core),
        "profile": profile,
        "topics_covered": [{"id": t, "label": TOPIC_LABELS[t]} for t in covered],
        "focus_topics": [{"id": t, "label": TOPIC_LABELS[t]} for t in focus],
        "mandatory": mandatory,
        "core": core,
    }
