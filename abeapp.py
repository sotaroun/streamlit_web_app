import streamlit as st
from PIL import Image
import random

# 手と画像を辞書で定義
oponent_hands = [
    {"name": "グー", "image": Image.open('data/gu.png')},
    {"name": "チョキ", "image": Image.open('data/tyoki.png')},
    {"name": "パー", "image": Image.open('data/pa.png')}
]

# ポイントをセッションで管理
if 'points' not in st.session_state:
    st.session_state.points = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'random_points_gu' not in st.session_state:
    st.session_state.random_points_gu = random.randrange(1, 10)
if 'random_points_tyoki' not in st.session_state:
    st.session_state.random_points_tyoki = random.randrange(1, 10)
if 'random_points_pa' not in st.session_state:
    st.session_state.random_points_pa = random.randrange(1, 10)

# タイトルと説明
def reset_game():
    st.session_state.points = 0
    st.session_state.game_over = False
    st.session_state.random_points_gu = random.randrange(1, 10)
    st.session_state.random_points_tyoki = random.randrange(1, 10)
    st.session_state.random_points_pa = random.randrange(1, 10)

def determine_result(player_hand, opponent_hand):
    if player_hand == opponent_hand:
        return "draw"
    elif (
        (player_hand == "グー" and opponent_hand == "チョキ") or
        (player_hand == "チョキ" and opponent_hand == "パー") or
        (player_hand == "パー" and opponent_hand == "グー")
    ):
        return "win"
    else:
        return "lose"

def choose_opponent_hand(player_hand, random_points):
    # 確率調整：次のポイントが6~9なら負ける確率90%
    if 6 <= random_points <= 9:
        if random.random() < 0.6:  # 60%の確率で負ける手
            if player_hand == "グー":
                return {"name": "パー", "image": Image.open('data/pa.png')}
            elif player_hand == "チョキ":
                return {"name": "グー", "image": Image.open('data/gu.png')}
            elif player_hand == "パー":
                return {"name": "チョキ", "image": Image.open('data/tyoki.png')}
    if 0 <= random_points <= 3:
        if random.random() < 0.3:  # 30%の確率で勝てる手
            if player_hand == "グー":
                return {"name": "チョキ", "image": Image.open('data/tyoki.png')}
            elif player_hand == "チョキ":
                return {"name": "パー", "image": Image.open('data/pa.png')}
            elif player_hand == "パー":
                return {"name": "グー", "image": Image.open('data/gu.png')}
    # 通常のランダム選択
    return random.choice(oponent_hands)

if st.session_state.game_over:
    st.title("GAME OVER")
    if st.button("もう一度遊ぶ"):
        reset_game()
else:
    st.title('じゃんけんゲーム')
    st.write('じゃんけんに勝って10ptを目指そう')
    st.caption(f'現在のポイント: {st.session_state.points}')

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(Image.open('data/gu.png'), width=50)
        st.caption(f'次のポイント: {st.session_state.random_points_gu}')
        gu_button = st.button("グー")
        if gu_button:
            chosen_hand = choose_opponent_hand("グー", st.session_state.random_points_gu)
            st.write(chosen_hand["name"])
            st.image(chosen_hand["image"], width=50)
            result = determine_result("グー", chosen_hand["name"])
            if result == "draw":
                st.write("もう一回")
            elif result == "lose":
                st.session_state.game_over = True
            elif result == "win":
                st.write("WIN")
                st.caption(f"獲得ポイント: {st.session_state.random_points_gu}")
                st.session_state.points += st.session_state.random_points_gu

    with col2:
        st.image(Image.open('data/tyoki.png'), width=50)
        st.caption(f'次のポイント: {st.session_state.random_points_tyoki}')
        tyoki_button = st.button("チョキ")
        if tyoki_button:
            chosen_hand = choose_opponent_hand("チョキ", st.session_state.random_points_tyoki)
            st.write(chosen_hand["name"])
            st.image(chosen_hand["image"], width=50)
            result = determine_result("チョキ", chosen_hand["name"])
            if result == "draw":
                st.write("もう一回")
            elif result == "lose":
                st.session_state.game_over = True
            elif result == "win":
                st.write("WIN")
                st.caption(f"獲得ポイント: {st.session_state.random_points_tyoki}")
                st.session_state.points += st.session_state.random_points_tyoki

    with col3:
        st.image(Image.open('data/pa.png'), width=50)
        st.caption(f'次のポイント: {st.session_state.random_points_pa}')
        pa_button = st.button("パー")
        if pa_button:
            chosen_hand = choose_opponent_hand("パー", st.session_state.random_points_pa)
            st.write(chosen_hand["name"])
            st.image(chosen_hand["image"], width=50)
            result = determine_result("パー", chosen_hand["name"])
            if result == "draw":
                st.write("もう一回")
            elif result == "lose":
                st.session_state.game_over = True
            elif result == "win":
                st.write("WIN")
                st.caption(f"獲得ポイント: {st.session_state.random_points_pa}")
                st.session_state.points += st.session_state.random_points_pa

if st.session_state.points >= 10:
    st.title("GAME CLEARおめでとう！")
    if st.button("もう一度遊ぶ"):
        reset_game()
