
from urllib import request
import bs4

url = "http://www.jma.go.jp/jp/week/328.html"
html = request.urlopen(url).read()

soup = bs4.BeautifulSoup(html, "html.parser")
res = soup.find_all(attrs={"class": "maxtemp"})

for i, e in enumerate(res):
	print(e.text[0:2])
