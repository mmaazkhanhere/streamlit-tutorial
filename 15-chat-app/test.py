import streamlit as st
from openai import OpenAI


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    layout="wide"  # Add this line to set the layout to wide
)

st.markdown("## Hello World Chat App!")

st.success("###### Streaming Chat Completions API!")

key = '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'

client = OpenAI(api_key=key)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[{"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages],
            stream=True,
        ):
            full_response += (response.choices[0].delta.content or "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append(
        {"role": "assistant", "content": full_response})