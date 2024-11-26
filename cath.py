import streamlit as st

# Set the title of the page
st.title("Student Biography: [Your Name]")

# Introduction Section
st.header("About Me")
st.image("cath.jpg", caption="This is me!", use_column_width=True)  # Replace with your photo path
st.write("""
    Hello! I'm **[Your Name]**, a student pursuing a degree in [Your Major] at [Your University]. 
    I am passionate about learning new things, exploring different fields, and contributing to the community. 
    On this blog, I'll share a little bit about my background, academic interests, projects, and more.
""")

# Academic Background Section
st.header("Academic Background")
st.write("""
    - Currently pursuing **[Degree]** in **[Your Major]** at **[Your University]**.
    - Expected graduation year: **[Year]**.
    - Some of the key subjects I am studying include **[Subject 1]**, **[Subject 2]**, and **[Subject 3]**.
    - Relevant skills: **[Skill 1]**, **[Skill 2]**, **[Skill 3]**.
""")

# Projects Section
st.header("My Projects")
st.write("""
    I am passionate about applying what I learn in real-world projects. Here are a few projects I have worked on:
""")

# List a couple of projects with descriptions
st.subheader("Project 1: [Project Name]")
st.write("""
    - **Description**: A brief overview of what the project is about.
    - **Tools Used**: [Tools/Languages used, e.g., Python, HTML, CSS, etc.]
    - **Link**: [Link to the project or GitHub repository if available]
""")

st.subheader("Project 2: [Project Name]")
st.write("""
    - **Description**: Another project description.
    - **Tools Used**: [Tools/Languages used]
    - **Link**: [Link to the project or GitHub repository]
""")

# Extracurricular Activities Section
st.header("Extracurricular Activities")
st.write("""
    In addition to my academic work, I am actively involved in:
    - **[Activity 1]**: A brief description of this activity.
    - **[Activity 2]**: A brief description of this activity.
    - **[Activity 3]**: A brief description of this activity.
""")

# Future Goals Section
st.header("My Future Goals")
st.write("""
    I am excited about my future as a [professional role you're aiming for, e.g., data scientist, software engineer, etc.].
    Some of my long-term goals include:
    - Expanding my knowledge in [topic of interest].
    - Working on [type of projects you want to focus on].
    - Contributing to open-source or community-driven initiatives.
""")

# Contact Information Section
st.header("Contact Me")
st.write("""
    Feel free to reach out if you'd like to connect or learn more about my work:
""")

# Links to social media or other contact methods
st.markdown("[Email me](mailto:your-email@example.com)")
st.markdown("[LinkedIn](https://www.linkedin.com/in/your-profile)")
st.markdown("[GitHub](https://github.com/your-profile)")

# Footer
st.write("© [Year] [Your Name]. All rights reserved.")
