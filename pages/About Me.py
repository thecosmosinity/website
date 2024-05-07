import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(page_title="About Me!", page_icon=":tada:", layout="wide")
st.sidebar.success("Select A Page!")

st.title("About Me!")

## Load Assets

def load(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

## Assets 
pookie = load("https://lottie.host/09b51c0e-7a6d-4533-9741-39a65bd39252/9RbLAiC8sM.json")

# Use Local CSS code
def css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
css("style/style.css")

with st.container():
    left, right = st.columns(2)
    with left:
        st.subheader("Hi! I am cosmosinity! :wave:")
        st.title("Your average programmer, I like to mess around with tech.")
        st.write("I love the colour white, I also like to code and use python to make some cool stuff!")
        st.write("[Redirects >](https://bento.me/cosmosinity)")

        st.write("learning python for a year :3")
    with right:
        st_lottie(pookie, height=500, key = "pookie :3")

st.write("© 2024 - 2024 cosmosinity - All Rights Reserved.")