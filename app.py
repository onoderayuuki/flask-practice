import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():
    """はてブのホットエントリーから記事を入手して、ランダムに1件返却します."""

    """
        **** ここを実装します（基礎課題） ****

        1. はてブのホットエントリーページのHTMLを取得する
        2. BeautifulSoupでHTMLを読み込む
        3. 記事一覧を取得する
        4. ランダムに1件取得する
        5. 以下の形式で返却する.
            {
                "content" : "記事のタイトル",
                "link" : "記事のURL"
            }
    """

    # Get
    with urlopen("https://b.hatena.ne.jp/hotentry/all") as res:
        html = res.read().decode("utf-8")
    #Load
    soup = BeautifulSoup(html,"html.parser")

    random = soup.select_one(".js-keyboard-openable")
    random_href = random.get("href")
    random_title = random.string
        
    return json.dumps({
        "content" : random_title,
        "link" : random_href
    })

@app.route("/api/hello")
def api_hello():
    """
        **** ここを実装します（発展課題） ****
        ・自分の好きなサイトをWebスクレイピングして情報をフロントに返却します
        ・お天気APIなども良いかも
        ・関数名は適宜変更してください
    """
    # Get
    with urlopen("http://www.helloproject.com/") as res:
        html = res.read().decode("utf-8")

    #Load
    soup = BeautifulSoup(html,"html.parser")

    #Select
    title = soup.select_one("#top_news > ul p a")
    hello_href = 'http://www.helloproject.com'+title.get("href")
    
    #画像取得
    with urlopen(hello_href) as res2:
        html2 = res2.read().decode("utf-8")
    soup2 = BeautifulSoup(html2,"html.parser")
    img = soup2.select_one("img")
    src = img.get("src")
    return json.dumps({
        "content" : title.text,
        "link" : hello_href,
        "src":src
    })

if __name__ == "__main__":
    app.run(debug=True, port=5004)
