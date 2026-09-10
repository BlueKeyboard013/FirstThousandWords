from typing import Dict, List

from pydantic import BaseModel, Field


class WordListRequest(BaseModel):
    language: str = Field(..., examples=["es", "fr"])
    answers: Dict[str, List[str]] = Field(
        default_factory=dict,
        description="Map of question id -> list of chosen option ids.",
        examples=[{"goal": ["travel"], "day": ["desk"]}],
    )
    core_size: int = Field(1000, ge=50, le=3000)


class WordEntry(BaseModel):
    rank: int
    word: str
    gloss: str
    topics: List[str]
    topic_labels: List[str]
    zipf: float


class MandatoryEntry(BaseModel):
    word: str
    gloss: str
    zipf: float


class TopicRef(BaseModel):
    id: str
    label: str


class WordListResponse(BaseModel):
    language: str
    language_name: str
    core_size: int
    profile: Dict[str, float]
    topics_covered: List[TopicRef]
    focus_topics: List[TopicRef]
    mandatory: List[MandatoryEntry]
    core: List[WordEntry]
