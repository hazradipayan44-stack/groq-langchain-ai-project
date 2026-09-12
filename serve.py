from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes
from dotenv import load_dotenv
load_dotenv()
groq_api_key=os.getenv("GROQ_API_KEY")


chat = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=groq_api_key
)



# --------------------------------------------------
# 6. Prompt Template
# --------------------------------------------------

generic_template = "Translate the following into {language}:"

prompt = ChatPromptTemplate.from_messages([
    ("system", generic_template),
    ("user", "{text}")
])

parser=StrOutputParser()

## Create Chain
chain=prompt|chat|parser

## App Definition
app=FastAPI(title="Langchain Server",
            version="1.0",
            description="A simple API server using Langchain runnable interfaces")


## Adding chain routes
add_routes(
    app,
    chain,
    path="/chain"

)
  


