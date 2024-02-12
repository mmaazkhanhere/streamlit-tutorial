import streamlit as st
from openai import OpenAI

st.title('Simple Chatbot')

key: str = st.text_input('Enter your OpenAI Secret Key: ', type='password')
st.markdown('<p style="font-size: 14px">Never share your API secret key on public platforms. This app is stateless and does not store anything in a database. Enter the key for app testing purposes only.</p>', unsafe_allow_html=True)

if key:
    
    client = OpenAI(api_key=key)
    
    if OpenAI(api_key=key):
        
        if 'openai_model' not in st.session_state:
            st.session_state['openai_model'] = 'gpt-3.5-turbo'
        
        if 'messages' not in st.session_state:
            st.session_state.messages = [
                {'role':'system', 'content':'You are a chatbot with name Kenuske'}
            ]

        for message in st.session_state.messages:
            # Skip the system message
            if message['role'] == 'system':
                continue
            with st.chat_message(message['role']):
                st.markdown(message['content'])
                
        prompt = st.chat_input("Ask me something...")

        if prompt:
            
            with st.chat_message('user', avatar="🦖"):
                st.markdown(prompt)
                
            st.session_state.messages.append({'role': 'user', 'content': prompt})
            
            with st.chat_message('assistant', avatar='🤖'):
                chat_placeholder = st.empty()
                assistant_response = ''
                
                for response in client.chat.completions.create(
                    model='gpt-3.5-turbo',
                    messages=[
                            {'role': m['role'], 'content': m['content']}
                            for m in st.session_state.messages],
                    stream=True,
                ):
                    if response.choices[0].delta.content is not None:
                        assistant_response += response.choices[0].delta.content
                        chat_placeholder.markdown(assistant_response + '||')
                chat_placeholder.markdown(assistant_response)
            st.session_state.messages.append({'role': 'assistant', 'content': assistant_response})
