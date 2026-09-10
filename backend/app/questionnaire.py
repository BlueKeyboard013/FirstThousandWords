"""The self-profiling questionnaire.

Each question has options; each option carries a dict of {topic: weight} that is
added up across all of the learner's answers to produce a topic-weight profile.
The engine then uses that profile to re-rank the word list.

The questionnaire is data, not code paths - add questions/options freely.
"""

from typing import Dict, List

QUESTIONS: List[dict] = [
    {
        "id": "goal",
        "prompt": "Why are you learning this language?",
        "help": "Pick everything that applies.",
        "multi": True,
        "options": [
            {"id": "travel", "label": "Travelling / holidays",
             "weights": {"travel_tourism": 3, "transport": 2, "city_places": 2,
                         "food_drink": 1}},
            {"id": "work", "label": "Work or business",
             "weights": {"work_office": 3, "technology": 1, "shopping_money": 1}},
            {"id": "family", "label": "Family, partner or friends who speak it",
             "weights": {"family": 3, "home_daily": 2, "social_emotions": 2}},
            {"id": "study", "label": "Study / passing an exam",
             "weights": {"school_study": 3, "arts_media": 1}},
            {"id": "living", "label": "Living in a country where it's spoken",
             "weights": {"home_daily": 2, "shopping_money": 2, "city_places": 2,
                         "health_body": 1, "transport": 1}},
            {"id": "culture", "label": "Books, films, music, culture",
             "weights": {"arts_media": 3, "social_emotions": 1}},
        ],
    },
    {
        "id": "day",
        "prompt": "What takes up most of your day?",
        "multi": False,
        "options": [
            {"id": "desk", "label": "A desk / office job",
             "weights": {"work_office": 3, "technology": 2}},
            {"id": "study", "label": "Studying",
             "weights": {"school_study": 3}},
            {"id": "trade", "label": "Hands-on or trade work",
             "weights": {"transport": 2, "home_daily": 2, "work_office": 1}},
            {"id": "care", "label": "Looking after family / the home",
             "weights": {"family": 3, "home_daily": 2, "food_drink": 2}},
            {"id": "health", "label": "Healthcare or caregiving",
             "weights": {"health_body": 3, "social_emotions": 1}},
            {"id": "service", "label": "Retail, hospitality or service work",
             "weights": {"shopping_money": 3, "food_drink": 2, "social_emotions": 1}},
        ],
    },
    {
        "id": "hobbies",
        "prompt": "What do you do in your free time?",
        "help": "Pick everything that applies.",
        "multi": True,
        "options": [
            {"id": "sport", "label": "Sport & fitness",
             "weights": {"sports_fitness": 3, "health_body": 1, "nature_weather": 1}},
            {"id": "cooking", "label": "Cooking & eating out",
             "weights": {"food_drink": 3}},
            {"id": "media", "label": "Reading, films & music",
             "weights": {"arts_media": 3}},
            {"id": "outdoors", "label": "Hiking & the outdoors",
             "weights": {"nature_weather": 3, "sports_fitness": 1}},
            {"id": "tech", "label": "Gaming & technology",
             "weights": {"technology": 3}},
            {"id": "social", "label": "Going out with friends",
             "weights": {"social_emotions": 3, "food_drink": 1, "city_places": 1}},
        ],
    },
    {
        "id": "audience",
        "prompt": "Who will you speak it with most?",
        "multi": False,
        "options": [
            {"id": "family", "label": "Family or in-laws",
             "weights": {"family": 3, "home_daily": 2}},
            {"id": "colleagues", "label": "Colleagues or clients",
             "weights": {"work_office": 3, "technology": 1}},
            {"id": "friends", "label": "Friends and peers",
             "weights": {"social_emotions": 3, "arts_media": 1}},
            {"id": "strangers", "label": "Shopkeepers, officials, strangers",
             "weights": {"shopping_money": 2, "city_places": 2, "transport": 2}},
        ],
    },
    {
        "id": "situation",
        "prompt": "Do any of these apply to you?",
        "help": "Pick everything that applies.",
        "multi": True,
        "options": [
            {"id": "kids", "label": "I have young children",
             "weights": {"family": 3, "health_body": 1}},
            {"id": "medical", "label": "I have health matters I'll need to discuss",
             "weights": {"health_body": 3}},
            {"id": "driving", "label": "I'll be driving or using public transport",
             "weights": {"transport": 3}},
            {"id": "housing", "label": "I'll be renting or buying a home",
             "weights": {"home_daily": 2, "shopping_money": 2, "city_places": 1}},
            {"id": "none", "label": "None of these", "weights": {}},
        ],
    },
]

_OPTION_INDEX = {
    q["id"]: {o["id"]: o for o in q["options"]} for q in QUESTIONS
}


def profile_from_answers(answers: Dict[str, List[str]]) -> Dict[str, float]:
    """answers: {question_id: [selected option ids]} -> {topic: weight}."""
    profile: Dict[str, float] = {}
    for qid, option_ids in answers.items():
        options = _OPTION_INDEX.get(qid, {})
        for oid in option_ids:
            option = options.get(oid)
            if not option:
                continue
            for topic, weight in option["weights"].items():
                profile[topic] = profile.get(topic, 0.0) + float(weight)
    return profile
