import csv
import io

from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware

from .engine import SUPPORTED_LANGUAGES, build_wordlist
from .models import WordListRequest, WordListResponse
from .questionnaire import QUESTIONS, profile_from_answers

app = FastAPI(title="First 1000 Words", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.get("/api/languages")
def languages():
    return [{"code": c, "name": n} for c, n in sorted(SUPPORTED_LANGUAGES.items())]


@app.get("/api/questionnaire")
def questionnaire():
    return {"questions": QUESTIONS}


def _build(req: WordListRequest) -> dict:
    if req.language not in SUPPORTED_LANGUAGES:
        raise HTTPException(400, f"Unsupported language: {req.language}")
    profile = profile_from_answers(req.answers)
    return build_wordlist(req.language, profile, core_size=req.core_size)


@app.post("/api/wordlist", response_model=WordListResponse)
def wordlist(req: WordListRequest):
    return _build(req)


@app.post("/api/wordlist.csv")
def wordlist_csv(req: WordListRequest):
    data = _build(req)
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["list", "rank", "word", "gloss", "topics", "zipf"])
    for e in data["mandatory"]:
        writer.writerow(["mandatory", "", e["word"], e["gloss"], "", e["zipf"]])
    for e in data["core"]:
        writer.writerow(
            ["core", e["rank"], e["word"], e["gloss"],
             "; ".join(e["topic_labels"]), e["zipf"]]
        )
    filename = f"first-1000-{data['language']}.csv"
    return Response(
        content=buf.getvalue(),
        media_type="text/csv",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )
