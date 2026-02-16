def analyze_cognitive_state(student):

    accuracy = student["accuracy"]
    attempts = student["attempts"]
    engagement = student["engagement"]

    if accuracy < 0.5 and attempts >= 3:
        confusion = "high"
    elif accuracy < 0.7:
        confusion = "medium"
    else:
        confusion = "low"

    if accuracy > 0.8:
        mastery = "high"
    elif accuracy > 0.6:
        mastery = "medium"
    else:
        mastery = "low"

    return {
        "confusion": confusion,
        "mastery": mastery,
        "engagement": engagement
    }
