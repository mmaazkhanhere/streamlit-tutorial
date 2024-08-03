

import streamlit as st

st.title('File Uploader')
st.markdown('----------------------------------------------------------------')

file_uploaded = st.file_uploader('Please upload an image', type=['png', 'jpg'])

if file_uploaded is not None:
    st.image(file_uploaded)