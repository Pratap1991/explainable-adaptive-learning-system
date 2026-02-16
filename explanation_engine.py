def generate_explanation(student, cognitive_state, decision):

    explanation = f"""
ADAPTIVE DECISION: {decision}

EVIDENCE:
Accuracy = {student['accuracy']}
Attempts = {student['attempts']}
Engagement = {student['engagement']}
Response Speed = {student['response_time']}

COGNITIVE STATE:
Confusion Level = {cognitive_state['confusion']}
Mastery Level = {cognitive_state['mastery']}

PEDAGOGICAL JUSTIFICATION:
Instruction is adapted based on cognitive load and mastery principles.

EXPECTED IMPACT:
Improved understanding and optimized learning progression.
"""

    return explanation
