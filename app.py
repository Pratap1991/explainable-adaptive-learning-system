import streamlit as st
import matplotlib.pyplot as plt

from student_simulator import generate_student
from learner_model import analyze_cognitive_state
from decision_engine import make_adaptive_decision
from explanation_engine import generate_explanation
from learning_simulator import simulate_learning_step
from metrics import compute_learning_gain, transparency_score

st.title("Explainable Adaptive Learning Research Simulator")

sessions = st.slider("Number of learning sessions", 5, 30, 10)

if st.button("Run Learning Simulation"):

    student = generate_student()
    initial_accuracy = student["accuracy"]

    accuracy_history = []

    for step in range(sessions):
        cognitive_state = analyze_cognitive_state(student)
        decision = make_adaptive_decision(cognitive_state)
        explanation = generate_explanation(student, cognitive_state, decision)

        student = simulate_learning_step(student, decision)
        accuracy_history.append(student["accuracy"])

    final_accuracy = student["accuracy"]
    gain = compute_learning_gain(initial_accuracy, final_accuracy)

    st.subheader("Initial Accuracy")
    st.write(initial_accuracy)

    st.subheader("Final Accuracy")
    st.write(final_accuracy)

    st.subheader("Learning Gain")
    st.success(gain)

    st.subheader("Transparency Score")
    st.write(transparency_score())

    st.subheader("Learning Progression")
    plt.plot(accuracy_history)
    plt.xlabel("Session")
    plt.ylabel("Accuracy")
    st.pyplot(plt)

    st.subheader("Final Explanation")
    st.text(explanation)
