import random

def generate_student():
    return {
        "accuracy": round(random.uniform(0.3, 0.7), 2),
        "attempts": random.randint(1, 5),
        "engagement": random.choice(["low", "medium", "high"]),
        "response_time": random.choice(["fast", "normal", "slow"])
    }
