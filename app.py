import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

chat = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

parser = StrOutputParser()

st.title("🤖 Groq + LangChain")

option = st.selectbox("Choose", ["Ask AI", "Translate"])

if option == "Ask AI":
    text = st.text_input("Ask anything")

    if st.button("Submit"):
        result = chat.invoke(text)
        st.write(result.content)

else:
    language = st.selectbox(
        "Translate to",
        ["French", "Hindi", "Bengali", "Spanish", "German"]
    )

    text = st.text_input("Enter text")

    if st.button("Translate"):
        prompt = ChatPromptTemplate.from_template(
            "Translate this into {language}: {text}"
        )

        chain = prompt | chat | parser

        result = chain.invoke({
            "language": language,
            "text": text
        })

        st.write(result)