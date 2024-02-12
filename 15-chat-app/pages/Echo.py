import streamlit as st

st.title("Echo Chatbot")

if 'messages' not in st.session_state:
    st.session_state.messages = []
    
for message in st.session_state.messages: #this section is responsible for displaying the chat history
    with st.chat_message(message['role']):
        st.markdown(message['content']) 
        
if prompt := st.chat_input('What is up'):
    with st.chat_message('user'):
        st.markdown(prompt)
        
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    
    response = f"Echo: {prompt}"
    
    with st.chat_message("assistant"):
        st.markdown(response)
        
    st.session_state.messages.append({'role': 'assistant', 'content': response})