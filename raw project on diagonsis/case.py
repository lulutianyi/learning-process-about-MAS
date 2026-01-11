# case.py

CASE = {
    "chief_complaint": "A 65-year-old male with fever and cough",
    "history": {
        "smoking": "40 pack-years smoking history",
        "duration": "Symptoms for 2 weeks"
    },
    "exam": {
        "lung": "Crackles in right lower lobe"
    },
    "lab": {
        "wbc": "Elevated white blood cell count"
    },
    "diagnosis": "Pneumonia"
}

def gatekeeper(query: str):
    query = query.lower()
    for section in ["history", "exam", "lab"]:
        if section in query:
            return CASE[section]
    return "No additional information."
