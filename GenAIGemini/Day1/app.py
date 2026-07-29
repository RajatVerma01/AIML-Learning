from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai 
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model=genai.GenerativeModel("gemini-2.5-flash")

def gemini_response(prompt):
    response = model.generate_content(
        prompt
    )
    return response.text


st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")

input=st.text_input("Input: ",key="input")


submit=st.button("Ask the question")


if submit:
    
    response=gemini_response(input)
    st.subheader("The Response is")
    st.write(response)