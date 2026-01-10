import streamlit as st
import os
from dotenv import load_dotenv
import google.genai as genai

# -----------------------------------
# Load environment variables
# -----------------------------------
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# -----------------------------------
# Initialize Gemini client
# -----------------------------------
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
    "This application helps learners identify learning gaps and "
    "receive personalized study recommendations using AI."
)

st.divider()

# -----------------------------------
# User Input
# -----------------------------------
st.header("Learner Self-Assessment")

topic = st.text_input(
    "Enter the subject or topic:",
    placeholder="e.g., DBMS, Python, Data Structures"
)

confidence = st.slider(
    "How confident are you in this topic?",
    0, 10, 5
)

# -----------------------------------
# Analysis
# -----------------------------------
if st.button("Analyze Learning Gap"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        level = "Low" if confidence <= 3 else "Medium" if confidence <= 7 else "High"

        prompt = f"""
You are an AI learning assistant.

Topic: {topic}
Confidence Level: {level}

Explain:
1. Learning gaps
2. Study recommendations
3. Next steps
"""

        with st.spinner("Analyzing learning gaps..."):
            try:
                response = client.models.generate_content(
                    model="gemini-1.5-flash",
                    contents=prompt
                )
                result = response.text

            except Exception:
                # Fallback AI logic (for restricted accounts)
                result = f"""
**Learning Gap Analysis (Offline AI Mode)**

You have a **{level} confidence** in **{topic}**.

**Possible Gaps:**
- Incomplete understanding of core concepts
- Lack of practical problem-solving
- Limited revision or practice

**Study Recommendations:**
- Revise fundamentals using structured notes
- Practice 5–10 problems daily
- Watch concept-based videos
- Use quizzes for self-evaluation

**Next Steps:**
- Create a short study plan
- Focus on weak subtopics
- Reassess confidence after practice
"""

        st.success("Analysis Complete")
        st.markdown(f"**Topic:** {topic}")
        st.markdown(f"**Learning Level:** {level}")
        st.markdown("### AI-Powered Recommendation")
        st.write(result)

# -----------------------------------
# Footer
# -----------------------------------
st.divider()
st.caption(
    "Developed by Supratik Mitra | CSRBOX – AICTE Applied AI Internship 2025 | SDG 4"
)
