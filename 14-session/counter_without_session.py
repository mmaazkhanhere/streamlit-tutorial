import streamlit as st

st.title('Counter Example')
count = 0

increment = st.button('Increment')  # whenever I click on button, it should
                            #increment counter
if increment:  # if button is clicked, increment counter
    count += 1

st.write('Count = ', count)  # display the value of counter

# it doesn't update after 1, because every time an action happens, the whole 
# page is rendered. The value of count becomes 0 and when clicked again, the
# value becomes 1. When clicked again, the whole page re-render, making the
# counter 0 and this process continues