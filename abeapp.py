import streamlit as st
from selenium import webdriver
from PIL import Image
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome import service as fs
from selenium.webdriver import ChromeOptions
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# タイトル
st.title('ィズニーグッズ情報')

# ボタンを作成(このボタンをアプリ上で押すと"if press_button:"より下の部分が実行される)

press_button = st.button("スクレイピング開始")

if press_button:
    # スクレイピングするwebサイトのURL
    URL = "https://www.buzzfeed.com/jp/bfjapan/disney-osusume-1-100"

    # ドライバのオプション
    options = ChromeOptions()

    # option設定を追加
    options.add_argument("--headless")
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # webdriver_managerによりドライバーをインストール

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # URLで指定したwebページを開く
    driver.get(URL)

    # グッズタイトルを取得
    goodsname = driver.find_element(By.CLASS_NAME, 'js-subbuzz__title-text').text
    st.caption(goodsname)

    


