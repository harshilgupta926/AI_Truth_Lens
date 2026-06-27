
import streamlit as st
from groq import Groq


st.set_page_config(
    page_title="VeriAI",
    page_icon="🧠"
)

st.title("🧠 VeriAI - AI Information Checker")
st.write(
    "Paste any claim, news, or information and AI will analyze its reliability."
)


api_key = st.sidebar.text_input(
    "Enter Groq API Key",
    type="password"
)


user_text = st.text_area(
    "Enter information:",
    placeholder="Example: Drinking lemon water cures every disease...",
    height=200
)


def analyze_information(text):

    client = Groq(api_key=api_key)

    prompt = f"""

You are an AI information analyst.

Analyze this information:

{text}


Give response in this format:

🔍 Claim Summary:
Explain the claim.

📊 Credibility Score:
Give score from 0-100 and reason.

⚠️ Possible Problems:
Find misleading or suspicious parts.

🎭 Bias Detection:
Identify emotional, marketing, or hidden bias.

🧠 Missing Context:
Explain missing important details.

⚖️ Balanced Explanation:
Give a neutral explanation.

Final Verdict:
Should people trust this information or verify more?

"""


    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3
    )


    return response.choices[0].message.content



if st.button("🔎 Analyze"):

    if not api_key:

        st.error("Please enter Groq API key")


    elif not user_text:

        st.warning("Please enter information")


    else:

        with st.spinner("AI is analyzing..."):

            result = analyze_information(user_text)


        st.success("Analysis Completed")

        st.markdown(result)



st.divider()

st.caption("Built with Python + Streamlit + Groq AI")

