from app.data.function_words import FUNCTION_WORD_SET
from app.engine import build_wordlist
from app.questionnaire import profile_from_answers


def test_core_excludes_function_words():
    result = build_wordlist("es", {}, core_size=1000)
    core_words = {e["word"] for e in result["core"]}
    assert not (core_words & FUNCTION_WORD_SET["es"])
    assert len(result["core"]) == 1000


def test_mandatory_list_is_populated_and_separate():
    result = build_wordlist("fr", {}, core_size=500)
    mandatory = {e["word"] for e in result["mandatory"]}
    assert {"le", "et", "je", "ne", "pas"} <= mandatory
    assert mandatory & {e["word"] for e in result["core"]} == set()


def test_profile_pushes_topic_words_up():
    plain = build_wordlist("es", {}, core_size=1000)
    traveller = build_wordlist("es", {"travel_tourism": 1.0}, core_size=1000)

    def rank_of(res, word):
        for e in res["core"]:
            if e["word"] == word:
                return e["rank"]
        return 10_000

    assert rank_of(traveller, "pasaporte") < rank_of(plain, "pasaporte")
    assert rank_of(traveller, "aeropuerto") <= rank_of(plain, "aeropuerto")


def test_curated_word_can_enter_list_via_profile():
    plain = build_wordlist("fr", {}, core_size=1000)
    health = build_wordlist("fr", {"health_body": 1.0}, core_size=1000)
    plain_words = {e["word"] for e in plain["core"]}
    health_words = {e["word"] for e in health["core"]}
    # something health-specific that a generic list may miss
    assert "pharmacie" in health_words
    assert len(health_words - plain_words) > 0


def test_profile_from_answers_accumulates():
    profile = profile_from_answers({"goal": ["travel", "work"], "day": ["desk"]})
    assert profile["work_office"] == 3 + 3  # goal:work + day:desk
    assert profile["travel_tourism"] == 3


def test_unsupported_language():
    try:
        build_wordlist("de", {})
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")
