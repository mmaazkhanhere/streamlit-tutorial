import streamlit as st

st.title('Streamlit application')
st.header('What makes streamlit special?')
st.subheader('It is beginner friendly')

st.text('I am learning streamlit to build AI powered applications')
st.markdown('I am learning streamlit to build AI powered applications') # everything written is a markdown\

st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}") #this is regex text

data = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}

st.json(data)

code = '''
def hello():
    print("Hello, World!")
'''

st.code(code, language='python')