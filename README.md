# 🧠 AI Truth Lens

An AI-powered information credibility analyzer built using Python, Streamlit, and Groq API.

AI Truth Lens helps users analyze claims, news, and documents by detecting possible misinformation, bias, and reliability issues. It provides a structured AI-generated report with credibility scoring and verification suggestions.

## 🚀 Features

- 🔍 AI Claim Analysis
- 📊 Credibility Score out of 10
- ⚖️ Truth Verdict (True / False / Partially True / Unverified)
- 🧩 Claim Breakdown
- 🎭 Bias & Manipulation Detection
- 📚 Reliable Source Suggestions
- 📄 PDF Document Analysis
- 🤖 AI-powered Investigation Report


## 🛠️ Tech Stack

- Python
- Streamlit
- Groq API
- Large Language Model (LLM)
- PyPDF


## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AI-Truth-Lens.git
````

Install required libraries:

```bash
pip install -r requirements.txt
```

## 🔑 Setup Groq API Key

Add your Groq API key inside the application sidebar.

Run the app:

```bash
streamlit run truth_lens.py
```

## 💡 How It Works

User enters information or uploads a PDF.

↓

AI extracts important claims.

↓

AI analyzes credibility, bias, and evidence strength.

↓

Generates a structured verification report.

## 📌 Example Output

```
CLAIM:
The Great Wall of China is visible from the Moon.

VERDICT:
❌ False

CREDIBILITY SCORE:
1/10

EVIDENCE FOUND:
No scientific evidence supports this claim.

BIAS DETECTION:
Common misinformation pattern detected.

RELIABLE SOURCES:
- NASA
- Scientific Research Papers

WHY:
The claim is a popular myth and lacks scientific proof.
```

## 🎯 Problem Statement

With the growth of online information, misinformation and misleading content are increasing.

AI Truth Lens helps users understand the reliability of information before believing or sharing it.

## 🔮 Future Improvements

* Real-time web fact checking
* Source comparison system
* News verification
* Image misinformation detection
* Browser extension
* AI confidence visualization

## 👨‍💻 Built With

Python + Streamlit + Groq AI

