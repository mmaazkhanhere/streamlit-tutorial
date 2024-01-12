import streamlit as st

st.title("Hello world! I am streamlit application")

st.header("This is header of the application ")

st.subheader("This is a subheader of the application")

st.text("This is simple **text** message")
# bold and italic works only for markdown

st.markdown("This is markdown *message* and this is **bold** text")
# ** wrapped text will be bold and * wrapped text will be italic
# all markdown style will be applicable like #H1, ##H2 etc.
st.markdown("# Headings")

st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

jsonFile = {"a": "1, 2, 3", "b": "4, 5, 6"}
st.json(jsonFile)

code = """
print("Hello world!")
"""

st.code(code)
