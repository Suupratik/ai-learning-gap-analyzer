# AI-Powered Personalized Learning Gap Analyzer 🎓

**Aligned with UN SDG 4 – Quality Education**

---

## 📌 Project Overview

The **AI-Powered Personalized Learning Gap Analyzer** is a web-based application that helps learners identify their knowledge gaps in any subject and receive **personalized learning recommendations**.

The system combines:

* **Rule-based logic** (confidence assessment)
* **Generative AI (Gemini API)** for intelligent feedback

This project demonstrates the practical use of **Applied AI** in the education domain, supporting **self-assessment, adaptive learning, and academic improvement**.

---

## 🎯 Objectives

* Enable learners to self-assess their understanding of a topic
* Identify possible learning gaps based on confidence levels
* Generate personalized study recommendations using AI
* Promote inclusive and quality education (SDG 4)

---

## 🧠 Problem Statement

Traditional learning systems:

* Do not adapt to individual confidence levels
* Lack personalized guidance
* Fail to identify *specific learning gaps*

This project addresses these issues using **AI-driven personalization**.

---

## 💡 Solution Approach

The application follows a **hybrid intelligence model**:

### 1. Rule-Based Layer

* User inputs:

  * Subject/topic
  * Confidence level (0–10)
* Confidence mapped to:

  * **Low**
  * **Medium**
  * **High**

### 2. AI Layer

* Uses **Google Gemini (Generative AI)** to:

  * Analyze learning gaps
  * Suggest personalized study strategies
  * Recommend next steps

---

## 🏗️ System Architecture (High-Level)

```
User Input
   ↓
Confidence Evaluation (Rule-Based Logic)
   ↓
Prompt Engineering
   ↓
Gemini AI Model
   ↓
Personalized Learning Recommendations
```
---

## 🛠️ Technologies Used

| Category               | Technology        |
| ---------------------- | ----------------- |
| Frontend               | Streamlit         |
| Backend                | Python            |
| AI Model | Google Gemini (Generative AI) |
| Environment Management | python-dotenv     |
| Version Control        | Git & GitHub      |

---

## 📂 Project Folder Structure

```
ai_learning_gap_analyzer/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
├── .gitignore             # Ignored files (env, cache, etc.)
├── .env                   # API key (NOT pushed to GitHub)
└── venv/                  # Virtual environment (local)
```

---

## 🧾 File Descriptions

### `app.py`

* Handles UI, logic, and AI integration
* Collects user inputs
* Generates AI-powered recommendations

### `requirements.txt`

* Contains all Python dependencies required to run the project

### `.env`

* Stores the **Gemini API key**
* Kept private for security reasons

### `.gitignore`

* Prevents sensitive and unnecessary files from being uploaded

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Suupratik/ai-learning-gap-analyzer.git
cd ai-learning-gap-analyzer
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Environment Variable

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at:

```
http://localhost:8501
```

---

## 🧪 How the Application Works

1. User enters a subject/topic
2. User selects confidence level (0–10)
3. System classifies learning level
4. AI analyzes gaps and generates:

   * Knowledge gap explanation
   * Study recommendations
   * Next learning steps

---

## 📊 Sample Output

* **Topic:** Python Basics
* **Confidence Level:** Medium
* **AI Recommendation:**

  * Revise loops and functions
  * Practice beginner-level coding problems
  * Refer to official Python documentation

---

## 🌍 SDG Alignment

### **UN Sustainable Development Goal 4 – Quality Education**

This project:

* Encourages self-learning
* Supports personalized education
* Improves accessibility to learning guidance

---

## 🚀 Future Enhancements

* User login & learning history
* Progress tracking dashboard
* Topic-wise quizzes
* Course recommendations with links
* Multi-language support

---

## 👨‍💻 Developer Details

**Name:** Supratik Mitra
**Program:** CSRBOX – AICTE Applied AI Internship 2025
**Domain:** Applied Artificial Intelligence
**Theme:** Education Technology 

---

## 🙏 Acknowledgements

* AICTE
* CSRBOX
* IBM SkillsBuild
* Google Gemini API

---

## 📌 Conclusion

The **AI-Powered Personalized Learning Gap Analyzer** demonstrates how **Applied AI** can enhance educational experiences through personalization, automation, and intelligent feedback — contributing meaningfully toward **quality education for all**.

---

