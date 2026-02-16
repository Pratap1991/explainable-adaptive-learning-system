def make_adaptive_decision(cognitive_state):

    if cognitive_state["confusion"] == "high":
        return "Reduce difficulty and provide revision"

    if cognitive_state["engagement"] == "low":
        return "Change teaching strategy to interactive content"

    if cognitive_state["mastery"] == "high":
        return "Increase difficulty and advance topic"

    return "Provide guided practice"
