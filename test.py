# %%
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Get
with urlopen("https://b.hatena.ne.jp/hotentry/all") as res:
    html = res.read().decode("utf-8")

#Load
soup = BeautifulSoup(html,"html.parser")

#Select
titles = soup.select(".js-keyboard-openable")
titles2 = [t.string for t in titles]


# %%
title = soup.select_one(".js-keyboard-openable")
print(title)
# %%
type(title)
# %%
print(title.get("href"))
print(title.string)

# %%
##########################################
from urllib.request import urlopen
from bs4 import BeautifulSoup
# Get
with urlopen("http://www.helloproject.com/") as res:
    html = res.read().decode("utf-8")

#Load
soup = BeautifulSoup(html,"html.parser")
# %%
#Select
title = soup.select_one("#top_news > ul p a")
print(title)
# %%
print(title.text)

# %%
print('http://www.helloproject.com'+title.get("href"))
# %%
#######################################
from urllib.request import urlopen
from bs4 import BeautifulSoup
with urlopen("http://www.helloproject.com/news/14043/") as res2:
        html2 = res2.read().decode("utf-8")
soup2 = BeautifulSoup(html2,"html.parser")
# %%
img = soup2.select_one("img")
# %%
img.get("src")
# %%
