import streamlit as st

st.title("My Portfolio")


col1, col2 = st.columns(2)

col1.header('A bit about me..')
col2.image('image.png', width=500)

st.write('My name is Maaz Khan who has extensive experience as a full stack developer, primarily using Nextjs, Tailwind CSS, TypeScript, REST API, and PostgreSQL. I have more than one year experience as junior machine learning engineer where I was part of a team who developed a predictive maintenance model for aircraft hydraulic engine. It was really exciting experience. What I like about development is that I am able to visualize how far I have come; how I created something form scratch. What I like about artifical intelligence is the prospect of making machines intelligent enough to take some load off from us. I am excited for such a future')