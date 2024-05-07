import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Contact Me!", page_icon=":love_letter:", layout="wide")
st.sidebar.success("Select A Page!")

st.title("Contact Me!")

# Use Local CSS code
def css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
css("style/style.css")

## Load Assets

def load(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

## Assets 
mail_bbg = load("https://lottie.host/d3d7d061-3a9c-4e65-9cd7-f340169fc2a6/TeMTqPbPKi.json")

with st.container():
    st.write("---")
    st.header("Get in Touch! :love_letter:")
    st.write("##")

    ## Docs at https://formsubmit.co/ !!! CHANGE EMAIL !!!

    contactform = """
    <form action="https://formsubmit.co/cosmosinity@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder='your name'required>
        <input type="email" name="email" placeholder='your email' required>
        <textarea name="message" placeholder="your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
"""

    left1, right1 = st.columns(2)
    with left1:
        st.markdown(contactform, unsafe_allow_html=True)
    with right1:
        st.empty()

    left, right = st.columns(2)
    with left:
        st.empty()
    with right:
        st_lottie(mail_bbg, height=200)
    st.write("psst! message me with the form to get your own website, paypal or rbx.")
    

st.write("© 2024 - 2024 cosmosinity - All Rights Reserved.")