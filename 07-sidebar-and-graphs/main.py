import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Dashboard")
st.sidebar.write("Sidebar")
opt = st.sidebar.radio("Select a graph: ", options=("Line", "Bar", "H-Bar"))

x = np.linspace(0, 10, 100)
bar_x: np.ndarray = np.array([1, 2, 3, 4, 5])

if opt == 'Line':
    st.header('Line Chart')
    fig = plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x))
    st.write(fig)

elif opt == "Bar":
    st.header('Bar Chart')
    fig = plt.figure()
    plt.bar(bar_x, bar_x * 10)
    st.write(fig)

elif opt == "H-Bar":
    st.header("Horizontal Bar")
    fig = plt.figure()
    plt.barh(bar_x, bar_x * 10)
    st.write(fig)