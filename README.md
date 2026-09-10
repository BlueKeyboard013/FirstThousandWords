# First 1000 Words

Work out the ~1000 words worth learning first in your target language, ranked
for **what you actually talk about**. Mandatory "glue" words (articles,
pronouns, prepositions, auxiliaries…) are kept in a separate list so they don't
eat into the 1000.

Languages: **Spanish**, **French** (more are just more data — see below).

## How it works

1. You answer a short questionnaire about yourself (why you're learning, your
   job, hobbies, who you'll talk to, life situation).
2. Each answer contributes weights to ~15 **topic modules** (family, travel,
   work, health, …), producing a personal topic profile.
3. The engine takes a frequency-ranked candidate pool from the
   [`wordfreq`](https://pypi.org/project/wordfreq/) corpus and re-scores every
   word as `frequency_score × (1 + boost × your_topic_weight)`. Hand-curated
   topic vocabulary (e.g. *pasaporte*, *pharmacie*) gets a floor so genuinely
   useful lower-frequency words can still make the cut.
4. Function words are filtered out of that list and returned separately.

Output: `core` (your 1000, each with an English gloss, topic tags and a Zipf
frequency) and `mandatory` (the glue words).

## Backend (Python — FastAPI)

```bash
cd backend
./run.sh                     # sets up .venv, installs deps, serves :8000
# interactive API docs: http://localhost:8000/docs
pytest                       # from backend/, with ../.venv/bin/python -m pytest
```

Key modules in [`backend/app`](backend/app):

| file | role |
|---|---|
| [`engine.py`](backend/app/engine.py) | scoring + list construction |
| [`questionnaire.py`](backend/app/questionnaire.py) | questions and answer→topic-weight mapping |
| [`data/function_words.py`](backend/app/data/function_words.py) | the mandatory glue-word lists |
| [`data/topics.py`](backend/app/data/topics.py) | curated per-topic vocabulary (seed data) |
| [`main.py`](backend/app/main.py) | FastAPI routes |

Endpoints: `GET /api/languages`, `GET /api/questionnaire`,
`POST /api/wordlist`, `POST /api/wordlist.csv`.

## Frontend (React + Vite + TypeScript)

```bash
cd frontend
npm install
npm run dev                  # http://localhost:5173, proxies /api to :8000
```

Three steps: pick language → questionnaire → results. Results view has search,
topic filter, CSV export, and "I know this" checkboxes persisted to
`localStorage`.

## Extending

- **More languages:** add the code to `SUPPORTED_LANGUAGES` in `engine.py`, then
  add its `FUNCTION_WORDS` and `TOPICS` entries. `wordfreq` already covers ~40
  languages for the frequency backbone.
- **Better coverage:** the topic word lists are intentionally small seed sets
  (~15 words each). Add more — the engine picks them up with no code changes.
- **Glosses for frequency-only words:** currently only curated words carry an
  English gloss; wiring in a bilingual dictionary would gloss the rest.
