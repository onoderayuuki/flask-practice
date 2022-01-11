## pyenv設定
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
pyenv global 3.8.0
python --version

## 仮想環境
- 作成
python -m venv demo
- 起動 
source demo/bin/activate
## 必要ライブラリのインストール
`Flask`と `BeautifulSoup` を使うのでそれらを `pip`でインストールします.
```
$ pip3 install --upgrade flask
$ pip3 install --upgrade beautifulsoup4
```
## 起動確認
まずは起動してみて動くことを確認します.
```
$ cd practice
$ python3 app.py
```
以下のURLでアクセス可能です。
```
http://localhost:5004
```

# 基礎課題
今日のニュースは？と問いかけて返答がある
→はてなブックマークのホットエントリー最上位リンクを紹介
# 発展課題
今日のハロプロは？と問いかけて返答がある
→HelloProject公式サイト(http://www.helloproject.com/)の新着ニュースリンクを紹介（写真付き）

