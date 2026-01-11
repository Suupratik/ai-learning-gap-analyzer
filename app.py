import streamlit as st

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="AI-Powered Personalized Learning Gap Analyzer",
    page_icon="📘",
    layout="centered"
)

# -----------------------------------
# App Header
# -----------------------------------
st.title("AI-Powered Personalized Learning Gap Analyzer")
st.subheader("SDG 4 – Quality Education")

st.write(
    """
    This application helps learners identify their learning gaps
    and receive personalized study recommendations using
    intelligent rule-based analysis.
    """
)

st.divider()

# -----------------------------------
# User Input Section
# -----------------------------------
st.header("Learner Self-Assessment")

topic = st.text_input(
    "Enter the subject or topic you want to evaluate:",
    placeholder="e.g., Python Basics, DBMS, Data Structures"
)

confidence = st.slider(
    "How confident are you in this topic?",
    min_value=0,
    max_value=10,
    value=5
)

# -----------------------------------
# Rule-Based Intelligence Engine
# -----------------------------------
def analyze_learning_gap(topic, confidence):
    if confidence <= 3:
        level = "Low"
        gap = (
            "You may lack foundational understanding of core concepts. "
            "There could be gaps in basics, terminology, and practical exposure."
        )
        recommendation = [
            "Start with beginner-level tutorials and textbooks",
            "Focus on basic concepts and definitions",
            "Practice simple examples and exercises",
            "Use visual learning resources such as videos"
        ]

    elif confidence <= 7:
        level = "Medium"
        gap = (
            "You have partial understanding but may face difficulty "
            "applying concepts to complex problems."
        )
        recommendation = [
            "Revise key concepts and formulas",
            "Solve intermediate-level problems",
            "Work on real-world examples or mini-projects",
            "Identify weak subtopics and revise them"
        ]

    else:
        level = "High"
        gap = (
            "Your understanding is strong, but there may be scope "
            "to improve depth, optimization, or advanced applications."
        )
        recommendation = [
            "Explore advanced topics and use cases",
            "Solve challenging problems",
            "Teach or explain concepts to others",
            "Apply knowledge through projects or research"
        ]

    return level, gap, recommendation

# -----------------------------------
# Analysis Trigger
# -----------------------------------
if st.button("Analyze Learning Gap"):
    if topic.strip() == "":
        st.warning("Please enter a topic before analysis.")
    else:
        with st.spinner("Analyzing learning gaps..."):
            level, gap, recommendations = analyze_learning_gap(topic, confidence)

        st.success("Analysis Complete")

        st.write(f"**Topic:** {topic}")
        st.write(f"**Learning Level:** {level}")

        st.subheader("Identified Learning Gap")
        st.write(gap)

        st.subheader("Personalized Study Recommendations")
        for i, rec in enumerate(recommendations, start=1):
            st.write(f"{i}. {rec}")

# -----------------------------------
# Footer
# -----------------------------------
st.divider()
st.caption(
    "Developed by Supratik Mitra | CSRBOX – AICTE Applied AI Internship 2025 | SDG 4"
)
