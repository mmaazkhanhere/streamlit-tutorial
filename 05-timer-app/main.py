import streamlit as st
import time as ts
from datetime import time

st.title("Countdown App")
time_value = st.time_input("Set Timer", value=time(0, 0, 0))  # initial value is 0

def convertor(time_str: str):
    """
    A fuction that takes time in HH:MM:SS format and converts it to total seconds
    """
    h, m, s = time_str.split(":")
    total_seconds = int(h) * 3600 + int(m) * 60 + int(s)
    return total_seconds

if str(time_value) == "00:00:00":
    st.write("Please set timer")  # ask user to set timer
else:
    seconds = convertor(str(time_value))  # converts the time into seconds

    bar = st.progress(0) # progress bar
    progress = st.empty() # the progress bar is set to 0
    countdown_text = st.empty() # the countdown text is set to empty

    for i in range(seconds, 0, -1):
        # loop from total seconds to 0 with step -1
        minutes, secs = divmod(i, 60) #divmod returns quotient and reminder
        hours, minutes = divmod(minutes, 60)
        
        countdown_text.text(f"Time remaining: {hours:02}:{minutes:02}:{secs:02}")
        bar.progress((seconds - i) / seconds)
        progress.text(f"{((seconds - i) / seconds) * 100:.2f}%")
        ts.sleep(1)

    countdown_text.text("Time's up!")
    progress.text("100%")
    bar.progress(1.0)
