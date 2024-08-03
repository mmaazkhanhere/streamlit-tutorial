import streamlit as st
import time as ts
from datetime import time


st.title('Countdown App')
time_value = st.time_input('Enter the time', value=time(0, 0, 0))

def convertor(time_value: str):
    """
        A function that takes a time string and returns the total time in seconds
    """
    hour, minute, seconds = time_value.split(":")
    total_seconds = int(hour) * 3600 + int(minute) * 60 + int(seconds)  
    return total_seconds

if time_value == '00:00:00':
    st.write("Please set the timer")
else:
    seconds = convertor(str(time_value))
    bar = st.progress(0)
    progress = st.empty()
    count_down_text = st.empty()

    for i in range(seconds, 0, -1):
        minutes, secs = divmod(i, 60)
        hour, minutes = divmod(minutes, 60)

        count_down_text.text(f"{hour:02d}:{minutes:02d}:{secs:02d}")
        bar.progress((seconds - i) / seconds)
        progress.text(f"{(seconds - i) / seconds * 100:.2f}%")
        ts.sleep(1)

count_down_text.text('Time is up')
progress.text('100%')
bar.progress(1.0)