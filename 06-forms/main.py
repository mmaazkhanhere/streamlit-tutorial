import streamlit as st

st.title("User Registration")

with st.form("Form 2"):
    col1, col2 = st.columns(2)
    first_name = col1.text_input('First Name', placeholder='Jane')
    last_name = col2.text_input('Last Name', placeholder = 'Doe')
    email_address = st.text_input('Email Address', placeholder = 'example@mail.com')
    password = st.text_input('Password', type='password')
    confirm_password = st.text_input('Confirm Password', type='password')
    state = st.form_submit_button("Submit")

if state:
    if first_name == "" and last_name == "":
        st.warning("Please enter required detail")
    elif password !=  confirm_password:
        st.warning("Password do not match")

    else:
        st.write(f"Full Name is: {first_name + "" + last_name}")
        st.write(f"Email address: {email_address}")