import streamlit as st

# The code is creating a user registration form using the Streamlit library in
# Python.
st.markdown(
    "<h1 style = 'text-align': center>User Registration</h1>", unsafe_allow_html=True
)

form = st.form("Form 1")
form.text_input("Enter username")
form.form_submit_button("Submit")


# The code block starting with `with st.form("Form 2"):` creates a second form
# in the user registration page. It uses the `st.columns()` function to create
# two columns, `col1` and `col2`, where the user can input their first name and
# last name respectively. It then checks if the user has entered the first
# and last names and password. If password is entered, it checks if the
# password is at least 5 characters. If not, it returns error messages else
# returns success message

with st.form("Form 2"):
    col1, col2 = st.columns(2)
    first_name: str = col1.text_input("First Name")
    last_name: str = col2.text_input("Last Name")
    email: str = st.text_input("Email Address")
    password: str = st.text_input("Enter password", type="password")
    state = st.form_submit_button("Submit")

if state:
    if first_name == "" and last_name == "" and password == "":
        st.warning("Please fill the above fields")
    elif len(password) <= 5:
        st.warning("Password must be at least 5 characters")
    else:
        st.success("Successfully submitted")
