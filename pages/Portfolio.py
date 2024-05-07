import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Portfolio", page_icon=":notebook:", layout="wide")
st.sidebar.success("Select A Page!")

st.title("Portfolio")

## Load Assets

def load(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

with st.container():
    left, right = st.columns(2)
    with left:
        st.header("Stuff I can do.")
        st.write("##")
        st.write('''
        Yo! I'm cosmosinity, I make content on YouTube and I love to play video games.

        - Mess around with tech every once in a while.
        - Emulate older tech.
        - Try out older unreleased software.
        - Play with code!
        - I also like to troll people. :)        

        ''')
        st.write("[Another cool website!](https://oguser.xyz/redirect)")

with st.container():
    st.write("---")
    left, right = st.columns(2)
    with left:
        st.header("Stuff I did/Acheivements.")
        st.write("##")
        st.write('''

        - 1 Year Python
        - 3 Years Content Creating and Editing
        - Intermediate Editor
        - Lot of Python Projects, Including this website!
        - Emulated/Have used over 100 Operating Systems

''')

with st.container():
    st.write("---")
    left, right = st.columns(2)
    with left:
        st.header("Python Stuff.")
        st.write("##")
        st.write('''

        - I can make webpages with python
        - Made discord bots with python
        - A lot of random projects (that i'm collecting) available at my github (https://github.com/thecosmosinity/python-archive) open for use by anybody that needs it!

''')

st.write("© 2024 - 2024 cosmosinity - All Rights Reserved.")
        