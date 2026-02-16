import random

def simulate_learning_step(student, decision):

    improvement = random.uniform(0.01, 0.05)

    if "Reduce difficulty" in decision:
        improvement += 0.03

    if "guided practice" in decision:
        improvement += 0.02

    if "advance topic" in decision:
        improvement += 0.01

    student["accuracy"] = min(1.0, student["accuracy"] + improvement)

    return student
