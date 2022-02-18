# pip install streamlit yaptiktan sonra masaustunde streamlit_notes klasorunu olusturdum.
# Klasorun icine app.py dosyasini olusturdum, terminalde klasorun icinde touch app.py
# Sonra, yine terminalde streamlit_notes klasorunun icinde streamlit run app.py yapiyoruz.
# Devami buradaki gibi

import streamlit as st

# Text/Title
st.title('Streamlit Tutorials')

# Header/Subheader
st.header('This is a header')
st.subheader('This is a subheader')

# Text
st.text('Hello Streamlit')

# Markdown
st.markdown('### This is a markdown')

# Error/Colorful Text
st.success('Succcessful')
st.info('Information')
st.warning('Warning')
st.error('Error')
st.exception("NameError('name three not defined')")

# Get help info about python
st.help(range)
st.help(list)

# Writing Text
st.write('Text with write')
st.write(range(10))

# Images
from PIL import Image
img = Image.open('image.jpeg')
st.image(img, width=300, caption='Simple Image')

# Videos
vid = open('video.mp4', 'rb')
vid_file = vid.read()
st.video(vid_file)

# Audio
audio_file = open('audio.mp3', 'rb').read()
st.audio(audio_file, format='audio/mp3')

# Widget -------
# Checkbox

if st.checkbox('Show/Hide'):
    st.text('Showing or Hiding Widgets')

# Radio
status = st.radio('What is you status?', ('Active', 'Inactive'))

if status == 'Active':
    st.success('You are Active')
else:
    st.warning('Warning, inactive')

# SelectBox
occupation = st.selectbox('Your occupation', ['Programmer', 'Data Scientist', 'Doctor'])
st.write('You selected this option', occupation)

# MultiSelect
location = st.multiselect('Where do you work?', ['London', 'Paris', 'New York', 'Istanbul'])
st.write('You selected', len(location), 'locations')

# Slider
age = st.slider('What is your age', 18, 90)
st.write('Your age is', age)

# Buttons
st.button('Simple button')
if st.button('About'):
    st.text('Streamlit is cool')

# How do you receive text input
firstname = st.text_input('Enter your firstname', 'Type here..')
if st.button('Submit'):
    result = firstname.title()
    st.success(result)

# Text Area
message = st.text_area('Enter your message', 'Type here..')
if st.button('Submitt'):
    result = message.title()
    st.info(result)

# Date Input
import datetime
today = st.date_input('Today is', datetime.datetime.now())

# Time
time = st.time_input('Time is', datetime.time())

# Displaying JSON
st.text('Display JSON')
st.json({'name':'Jessie', 'gender':'male'})

# Display Raw Code
st.text('Display Raw Code')
st.code('import numpy as np')

# Display Raw Code
with st.echo():
    # This will also be shown as a comment
    import pandas as pd
    df = pd.DataFrame()

# Progress Bar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 10)

# Spinner
with st.spinner('Waiting ..'):
    time.sleep(1)
st.success('Finished')

# Balloons
st.balloons()

# Sidebars
st.sidebar.header('About')
st.sidebar.text('This is Streamlit')

# Functions
@st.cache
def run_multiple():
    return range(100)
st.write(run_multiple())

# Plot
st.pyplot()

# DataFrames
st.dataframe()

# Table
st.table()