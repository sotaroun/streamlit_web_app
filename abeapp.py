import streamlit as st
from PIL import Image

st.title('アベアプリ')
st.caption('これは安部のテストアプリです')

image = Image.open('./data/abeimage.webp')
st.image(image, width=200)