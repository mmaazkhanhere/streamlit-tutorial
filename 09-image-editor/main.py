import streamlit as st
from PIL import Image
from PIL.ImageFilter import *

st.markdown("<h1 style='text-align: center;'>Image Editor</h1>", unsafe_allow_html=True)
st.markdown("---")
image = st.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg'])

info = st.empty()
size = st.empty()
mode = st.empty()
format = st.empty()

if image:
    img = Image.open(image)
    st.image(img)
    
    info.markdown("<h2 style='text-align:center;'>Information</h2>", unsafe_allow_html=True)
    
    size.markdown(f"<h6>Size: {img.size} </h6>", unsafe_allow_html=True)
    mode.markdown(f"<h6>Mode: {img.mode} </h6>", unsafe_allow_html=True)
    format.markdown(f"<h6>Format: {img.format} </h6>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align:center;'>Resizing</h2>", unsafe_allow_html=True)
    width = st.number_input("Width", value=img.width)
    height = st.number_input("Height", value=img.height)
    
    st.markdown("<h2 style='text-align:center;'>Rotation</h2>", unsafe_allow_html=True)
    degree = st.number_input("Degree")
    
    st.markdown("<h2 style='text-align:center;'>Filters</h2>", unsafe_allow_html=True)
    filters = st.selectbox("Filters", options=("None", "Blur", "Detail", "Emboss", "Smooth"))
    
    state = st.button("Submit")
    
    if state:
        resized_image = img.resize((width, height)).rotate(degree)
        filtered_image = resized_image
        if filters != 'None':
            if filters == 'Blur':
                filtered_image = resized_image.filter(BLUR)
            elif filters == "Detail":
                filtered_image = resized_image.filter(DETAIL)
            elif filters == "Emboss":
                filtered_image = resized_image.filter(EMBOSS)
            else:
                filtered_image = resized_image.filter(SMOOTH)
                
        st.image(filtered_image)