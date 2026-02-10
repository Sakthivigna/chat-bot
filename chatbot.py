import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyAeYETIDt6chz3Wlia0Hc_jEoPzxCxrRYI")

model = genai.GenerativeModel("models/gemini-2.5-flash")

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

st.title("Gemini Chatbot")

user_input = st.text_input("You")

if user_input:
    response = st.session_state.chat.send_message(user_input)
    st.write(response.text)
