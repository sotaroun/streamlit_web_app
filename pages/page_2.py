import streamlit as st

with st.form(key='profile_form'):
    name = st.text_input('名前')
    address = st.text_input('住所')

    age_category = st.radio(
        '年齢層'
        ('子供(18歳未満)', '大人(18歳以上)'))
    
    submit_btn = st.form_submit_button('送信')
    submit_btn = st.form_submit_button('キャンセル')

    if submit_btn:
        st.text(f'ようこそ！{name}さん！{address}に書類を送りました！')  
        st.text(f'年齢層：{age_category}')