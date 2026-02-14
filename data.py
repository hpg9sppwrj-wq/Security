import requests
import streamlit as st

st.set_page_config(page_title = 'Edwin Flores - Journey Vlog', layout = 'wide')

img_space_shuttle = 'Space Shuttle.png'
img_contact_form = 'Ideal Rocket Equation_1.png'
img_contact_form_2 = 'Ideal Rocket Equation_4.png'

st.subheader("Hi, I'm Edwin Flores :v:")
st.title('An Aspiring Aerospace Engineer, Musician, and Life Vlogger')
st.write("""
         I'm passionate about creating content that combines my interests in technology, 
         music, and storytelling. Join me on my journey as I explore the world of coding, 
         share my musical experiences, and document my life adventures!
         """)
st.write("[My GitHub >](https://github.com/hpg9sppwrj-wq)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write("""
                 I'm Edwin Flores, an aspiring aerospace engineer with a love for 
                 music and vlogging. I enjoy sharing my knowledge and experiences 
                 through engaging content. Whether it's coding projects, music covers, 
                 or life vlogs, I aim to inspire and connect with my audience.
                 """)
        st.write("[YouTube Channel >](https://youtube.com/@edw_flores10)")
    with right_column:
        st.image(img_space_shuttle, width = 600,)

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    
    with text_column:
        st.subheader('Aerospace for Python | Ideal Rocket Equation - Part 1')
        st.write("""
                In this video, we program a calculator in Python to find the change in velocity of 
                a rocket using the Ideal Rocket Equation. This is part one of a series on aerospace
                engineering concepts implemented in Python.
                 """)
        st.markdown('[Watch Video >](https://www.youtube.com/watch?v=f4-miRHYeEc)')

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form_2)

    with text_column:
        st.subheader('Aerospace for Python | Ideal Rocket Equation - Part 4')
        st.write("""
                In this video, we finish our exploration of the Ideal Rocket Equation and the pilot with
                calculator in Python to determine the thrust/burn time of a rocket based on your desired 
                rocket parameters. Stay tuned for more of!
                 """)
        st.markdown('[Watch Video >](https://www.youtube.com/watch?v=d68WeQ4DJJk)')