# The code you provided is a Python script that uses the Streamlit library to
# create a web application with a sidebar and different types of graphs. Here's a
# breakdown of what the code does:

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Sidebar in streamlit")
st.sidebar.write("This is sidebar in streamlit")
opt = st.sidebar.radio("Select any graph", options=("Line", "Bar", "H-Bar"))
x: np.ndarray = np.linspace(0, 10, 100)
bar_x: np.ndarray = np.array([1, 2, 3, 4, 5])

if opt == "Line":
    st.markdown(
        "<h1 style = 'text-align': center>Line Chart</h1>", unsafe_allow_html=True
    )
    fig = plt.figure()
    plt.style.use(
        "https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle"
    )
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x), "--")
    st.write(fig)

elif opt == "Bar":
    st.markdown(
        "<h1 style = 'text-align': center>Bar Chart</h1>", unsafe_allow_html=True
    )
    fig = plt.figure()
    plt.style.use(
        "https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle"
    )
    plt.bar(bar_x, bar_x * 10)
    st.write(fig)

elif opt == "H-Bar":
    st.markdown(
        "<h1 style = 'text-align': center>Horizontal Bar Chart</h1>",
        unsafe_allow_html=True,
    )
    fig = plt.figure()
    plt.style.use(
        "https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle"
    )
    plt.barh(bar_x * 10, bar_x)
    st.write(fig)
