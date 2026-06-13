import streamlit as st
from chatbot import chatbot

st.title("AmazonAssist AI")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "last_product" not in st.session_state:
    st.session_state.last_product = None

query = st.text_input("Ask a question")

if st.button("Send"):

    response, product = chatbot(
        query,
        st.session_state.last_product
    )

    if product:
        st.session_state.last_product = product

    st.session_state.chat_history.append(
        {
            "question": query,
            "answer": response
        }
    )

for chat in reversed(st.session_state.chat_history):

    st.write("👤 User:", chat["question"])
    st.write("🤖 Bot:", chat["answer"])
    st.write("---")