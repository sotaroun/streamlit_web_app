import streamlit as st
from PIL import Image
import random

# 手と画像を辞書で定義
oponent_hands = [
    {"name": "グー", "image": Image.open('data/gu.png')},
    {"name": "チョキ", "image": Image.open('data/tyoki.png')},
    {"name": "パー", "image": Image.open('data/pa.png')}
]

# タイトルと説明
st.title('じゃんけんゲーム')
st.write('じゃんけんに勝って10ptを目指そう')

# カラムでボタンを配置
col1, col2, col3 = st.columns(3)

with col1:
    gu_button = st.button("グー")
    st.image(Image.open('data/くgu.png'), width=50)
    st.write(random.randrange(10), 'pt')
    if gu_button:
        chosen_hand = random.choice(oponent_hands)
        st.write(chosen_hand["name"])
        st.image(chosen_hand["image"], width=50)

with col2:
    tyoki_button = st.button("チョキ")
    st.image(Image.open('data/tyoki.png'), width=50)
    st.write(random.randrange(10), 'pt')
    if tyoki_button:
        chosen_hand = random.choice(oponent_hands)
        st.write(chosen_hand["name"])
        st.image(chosen_hand["image"], width=50)

with col3:
    pa_button = st.button("パー")
    st.image(Image.open('data/pa.png'), width=50)
    st.write(random.randrange(10), 'pt')
    if pa_button:
        chosen_hand = random.choice(oponent_hands)
        st.write(chosen_hand["name"])
        st.image(chosen_hand["image"], width=50)
