import streamlit as st

st.set_page_config(page_title="Wesite", page_icon=":tata:", layout="wide")

st.subheader('Hi, I am Aniket :wave:')
st.title("A Tech Entusiast from India")
st.write('I love to code and build software which people love and also build robots like Iron man.')
st.write('[My Youtube Channel  >](https://www.youtube.com/channel/UCBmfbUZZ6jvGZV3DFL0p7LA/videos)')

st.write("----")

st.write('[Hangman Game in Python](https://replit.com/@aniketcoder123/Hangman-Game#main.py)')
st.write("")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
local_css("style.css")