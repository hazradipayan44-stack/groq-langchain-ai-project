
# import os
# from dotenv import load_dotenv
# from langchain_core import messages
# from langchain_groq import ChatGroq

# load_dotenv()

# groq_api_key = os.getenv("GROQ_API_KEY")

# print("API key loaded:", bool(groq_api_key))

# chat = ChatGroq(
#     model="openai/gpt-oss-20b",
#     api_key=groq_api_key
# )

# response = chat.invoke("What is the capital of France?")

# print("Response:")
# print(response.content)

# from langchain_core.messages import HumanMessage,SystemMessage

# messages=[
#     SystemMessage(content="Translate the following from English to French"),
#     HumanMessage(content="hello how are you?")
# ]
# result=chat.invoke(messages)
# print(result.content)

# from langchain_core.output_parsers import StrOutputParser
# parser=StrOutputParser()
# parser.invoke(result)

# ## Using LCEL chain the components
# chain=chat|parser
# chain.invoke(messages)



# # ## Prompt Templates
# # from langchain_core.prompts import ChatPromptTemplate
# # generic_template="Translate the following into {language}:" 
# # prompt=ChatPromptTemplate.format_messages(
# #     [
# #         ("system",generic_template),("user","{text}")
# #     ]
# # )

# # prompt.invoke({"language":"French","text":"hello"})

# # chain=prompt|chat|parser
# # chain.invoke({"language":"French","text":"hello"})



import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


# --------------------------------------------------
# 1. Load API key
# --------------------------------------------------

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

print("API key loaded:", bool(groq_api_key))


# --------------------------------------------------
# 2. Create ChatGroq model
# --------------------------------------------------

chat = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=groq_api_key
)


# --------------------------------------------------
# 3. Simple question
# --------------------------------------------------

response = chat.invoke(
    "What is the capital of France?"
)

print("\nSimple Response:")
print(response.content)


# --------------------------------------------------
# 4. Using SystemMessage + HumanMessage
# --------------------------------------------------

messages = [
    SystemMessage(
        content="You are a helpful language translator."
    ),
    HumanMessage(
        content="Translate 'Hello, how are you?' into French."
    )
]

response = chat.invoke(messages)

print("\nMessage Response:")
print(response.content)


# --------------------------------------------------
# 5. Output Parser
# --------------------------------------------------

parser = StrOutputParser()

parsed_response = parser.invoke(response)

print("\nParsed Response:")
print(parsed_response)


# --------------------------------------------------
# 6. Prompt Template
# --------------------------------------------------

generic_template = "Translate the following into {language}:"

prompt = ChatPromptTemplate.from_messages([
    ("system", generic_template),
    ("user", "{text}")
])


# --------------------------------------------------
# 7. LCEL Chain
# --------------------------------------------------

chain = prompt | chat | parser


# --------------------------------------------------
# 8. Run the complete chain
# --------------------------------------------------

result = chain.invoke({
    "language": "French",
    "text": "Hello, how are you?"
})

print("\nFinal Chain Response:")
print(result)