import streamlit as st
from groq import Groq
from pypdf import PdfReader


st.set_page_config(
    page_title="AI Truth Lens",
    page_icon="🧠",
    layout="centered"
)


st.title("🧠 AI Truth Lens")

st.subheader("See beyond the information you consume.")

st.write(
    "An AI-powered credibility analyzer that checks claims, detects bias and evaluates reliability."
)


api_key = st.sidebar.text_input(
    "Enter Groq API Key",
    type="password"
)



def read_pdf(file):

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text



def analyze(text):

    client = Groq(
        api_key=api_key
    )


    prompt = f"""

You are an AI Truth Verification Analyst.

Analyze this information:

{text}


Give ONLY a concise structured report:

CLAIM:
Extract the main claim.


VERDICT:
Choose one:
✅ True
⚠️ Partially True
❌ False
❓ Unverified


CREDIBILITY SCORE:
Give score out of 10.


CLAIM BREAKDOWN:
Break the information into important claims.


EVIDENCE FOUND:
Give possible supporting or contradicting evidence.


EVIDENCE STRENGTH:
Rate:
Strong / Medium / Weak


BIAS DETECTION:
Detect:
- Emotional language
- Manipulation
- Exaggeration


RELIABLE SOURCES:
Suggest where this information should be verified.

Examples:
- Scientific papers
- Government websites
- Trusted organizations


WHY:
Give a short final explanation.


Keep it clear and professional.

"""


    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],

        temperature=0.2
    )


    return response.choices[0].message.content



method = st.radio(

    "Choose input:",

    [
        "Text",
        "Upload PDF"
    ]

)


content = ""


if method == "Text":

    content = st.text_area(

        "Enter information:",

        height=220,

        placeholder="Example: The Great Wall of China is visible from Moon..."
    )


else:

    file = st.file_uploader(

        "Upload PDF",

        type=["pdf"]

    )


    if file:

        content = read_pdf(file)



if st.button("🔍 Analyze Information"):


    if not api_key:

        st.error(
            "Please enter Groq API Key"
        )


    elif not content:

        st.warning(
            "Enter text or upload PDF"
        )


    else:


        with st.spinner(
            "AI Investigator analyzing..."
        ):

            result = analyze(content)



        st.success(
            "Analysis Completed"
        )


        st.markdown(result)



st.divider()

st.caption(
    "AI Truth Lens | Python + Streamlit + Groq AI"
)