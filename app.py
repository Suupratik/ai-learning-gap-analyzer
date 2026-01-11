import streamlit as st
import google.genai as genai

# -----------------------------------
# API KEY (REPLACE VALUE ONLY)
# -----------------------------------
API_KEY = "AIzaSyBj7hDSAXa2XzRO1BHVjdBDutWL3Ey9KwI"

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)

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
    and receive personalized study recommendations using AI.
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
# Hybrid Logic: Rule-based + AI
# -----------------------------------
if st.button("Analyze Learning Gap"):
    if topic.strip() == "":
        st.warning("Please enter a topic before analysis.")
    else:
        # Rule-based classification (fallback logic)
        if confidence <= 3:
            level = "Low"
        elif confidence <= 7:
            level = "Medium"
        else:
            level = "High"

        prompt = f"""
You are an AI learning assistant.

A student is learning the topic "{topic}".
Their confidence level is "{level}".

Provide:
1. A brief explanation of the learner's possible knowledge gaps
2. Personalized study recommendations
3. Suggested next steps to improve understanding

Keep the response concise, structured, and educational.
"""

        with st.spinner("AI is analyzing learning gaps..."):
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=prompt
            )

        st.success("Analysis Complete")
        st.write(f"**Topic:** {topic}")
        st.write(f"**Learning Level:** {level}")
        st.write("**AI-Powered Recommendation:**")
        st.write(response.text)

# -----------------------------------
# Footer
# -----------------------------------
st.divider()
st.caption(
    "Developed by Supratik Mitra | CSRBOX – AICTE Applied AI Internship 2025 | SDG 4"
)
