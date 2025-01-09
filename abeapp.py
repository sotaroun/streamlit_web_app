import streamlit as st
from selenium import webdriver
from PIL import Image
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome import service as fs
from selenium.webdriver import ChromeOptions
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.common.by import By

# タイトル
st.title('ディズニーグッズ情報')

# ボタンを作成(このボタンをアプリ上で押すと"if press_button:"より下の部分が実行される)

press_button = st.button("スクレイピング開始")

if press_button:
    # スクレイピングするwebサイトのURL
    URL = "https://www.tokyodisneyresort.jp/tdl/shop.html"

    # ドライバのオプション
    options = ChromeOptions()

    # option設定を追加
    options.add_argument("--headless")
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # webdriver_managerによりドライバーをインストール
    # chromiumを使用したいのでchrome_type引数でchromiumを指定しておく
    CHROMEDRIVER = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
    service = fs.Service(CHROMEDRIVER)
    driver = webdriver.Chrome(
                                options=options,
                                service=service
                                )
    # URLで指定したwebページを開く
    driver.get(URL)

    # webページ上の最新項目をクリック
    newgoods = driver.find_element(By.CLASS_NAME, 'listTextArea')
    newgoods.click()

    # グッズタイトルを取得
    goodsname = driver.find_element(By.TAG_NAME, 'heading1')
    st.caption(goodsname)

    # webページ上のタイトル画像を取得
    img = driver.find_element(By.XPATH, '//div[@id="page"]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/img')
    src = img.get_attribute('src')

    # 取得した画像をカレントディレクトリに保存
    with open(f"tmp_img.png", "wb") as f:
        f.write(img.screenshot_as_png)

    # 保存した画像をstreamlitアプリ上に表示
    st.image("tmp_img.png")

    # webページを閉じる
    driver.close()

    # スクレイピングが完了したことをstreamlitアプリ上に表示する
    st.write("スクレイピング完了！")

    st.caption('これは安部のテストアプリです')


