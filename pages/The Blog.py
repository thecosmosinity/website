import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Blog", page_icon="📬", layout="wide")
st.sidebar.success("Select A Page!")

st.title("Blog/Projects")

def load(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

cat_pookie = ".assets/cat-pfp-black.jpg"

with st.container():
    st.write("---")
    st.header("The Blog!")
    st.write("##")
    image, text = st.columns((1, 2))

    with image:
        st.image(cat_pookie)
    with text:
        st.subheader("The Ultimate Gaming PC!")
        st.write('''
        19-04-2024, Friday
                 
        This was by far, my hardest project. After all, i only had scrap parts ;-;.
        This project was made ENTIRELY by scrap laptops.
                 
        One day, I was bored, and I thought, 'why don't i make a gaming laptop, it can't be that hard, right?'
        I took out 3 old laptops, and selected an HP ProBook 6460b as my base.
        I also had an ancient Toshiba Portege and a newer ProBook.
                 
        The reason I took the older model was because the new ProBook opens from the keyboard,
        and, the 6460b had a faster CPU and more RAM. I decided to put an SSD in and slotted in 8 gigs of ram.
        I installed Windows 10 and currently have the bare minimum drivers... I have more but there were hardly 3 installed...
        
        Soon, when I feel like it, I'll run benchmarks and install games, but till then,
        we won't have any updates.
                 
        Expect an update by late April, peace!

        ''')

st.write("© 2024 - 2024 cosmosinity - All Rights Reserved.")