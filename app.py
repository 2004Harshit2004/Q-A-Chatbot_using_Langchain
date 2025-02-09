from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()

import os

import streamlit as st

## function to load openai model and get response

def get_response(question):
    llm=OpenAI(openai_api_key=os.getenv("OPENAI_API"),temperature=0.5,model_name="text-davinci-003")
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

