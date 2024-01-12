import streamlit as st
import time as ts
from datetime import time

st.title("Timer App")  # title for the timer
val = st.time_input("Set Timer", value=time(0, 0, 0))
# the user selects the timer from the list with initial value of 00: 00: 00


def converter(value: str):
    """
    Takes a string representing a time value and converts it into a
    total time in seconds
    """
    m, s, mm = value.split(":")  # splits the time into mins, secs and millsec
    t_s = int(m) * 60 + int(s) + int(mm) / 1000
    # int(m * 60) converts minute to seconds
    # int(s) adds the seconds
    # int(mm) converts milliseconds to seconds
    return t_s  # returns the total second


if str(val) == "00:00:00":
    st.write("Please set timer")  # ask user to set timer
else:
    sec = converter(str(val))  # converts the time into seconds
    bar = st.progress(0)  # progress bar with initial value set to
    per = sec / 100  # percentage per iteration
    progress_status = st.empty()
    for i in range(100):
        bar.progress((i + 1))  # progress bar is updated
        progress_status.write(str(i) + "%")  # value of progress bar printed
        ts.sleep(per)  # introduces a delay
