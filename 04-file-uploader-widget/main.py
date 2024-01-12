import streamlit as st

st.title("Uploading Files")
st.markdown("----------------------------------------------------------------")
uploaded_image = st.file_uploader(
    "Please upload an Image", type=["png", "jpg"], accept_multiple_files=True
)
if uploaded_image is not None:
    st.image(uploaded_image)
