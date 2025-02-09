from langchain_community.llms import HuggingFaceHub

from dotenv import load_dotenv
load_dotenv()

import os

import streamlit as st

def get_response(question):
    llm=HuggingFaceHub(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        huggingfacehub_api_token=os.getenv("HUGGINGFACE_API"),
        model_kwargs={"temperature": 0.6, "max_length": 64}
                        )
    response=llm(question)
    return response



## Intialize streamlit app

st.set_page_config(page_title="Q-A Demo")

st.header("Q-A Chatbot using Langchain")

submit = st.button("Generate")

input = st.text_input("input :",key="input")
response=get_response(input)

## If button is clicked

if submit:
    st.subheader("The Response is : ")
    st.write(response)

