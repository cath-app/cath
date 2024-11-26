import streamlit as st

# Title
st.title("Student Biography: Catherine T. Dumagtoy")

st.header("About Me")
st.image("cath.jpg", caption="This is me!", use_column_width=True)
st.write("""
    Hello! I'm **Catherine**, a student pursuing a degree in **Bachelor of Science in Computer Engineering** at **Surigao Del Norte State University**. 
    On this blog, I'll share a little bit about my background, academic interests, projects, and more.
""")

st.header("Personal Details")
st.write("""
    - **Full Name**: Catherine T. Dumagtoy
    - **Date of Birth**: July 2, 2006
    - **Gender**: Female
    - **Location**: Surigao City, Philippines
    - **Nationality**: Filipino
""")

# Educational Attainment
st.header("Educational Attainment")
st.subheader("Elementary School")
st.write("""
    - **School Name**: Surigao West Central Elementary School
    - **Duration**: 2013 - 2018
""")
st.subheader("High Scool")
st.write("""
    - **School Name**: Surigao City National High School
    - **Duration**: 2018 - 2024
""")

st.header("My Interests")
st.write("""
    In addition to my professional work, I enjoy **Reading** and **Listening to music**. 
    Some of my favorite activities include:
    - Watching movies
    - Playing video games
    - Sleeping
""")

st.header("Contact Me")
st.markdown("[Email Me](mailto:your-dumagtoycatherine29@gmail.com)")
