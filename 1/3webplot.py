
from urllib import request
import bs4
from matplotlib import pyplot

url = "http://www.jma.go.jp/jp/week/328.html"
html = request.urlopen(url).read()

soup = bs4.BeautifulSoup(html, "html.parser")

y = []
tds = soup.find_all("td", {"class": "for"})

for i, e in enumerate(tds):
	day = e.find_all("font", {"class": "maxtemp"})
	if len(day) >= 1:
		y.append(int(day[0].text[0:2]))

x = []
days = soup.find_all(attrs={"class": ["weekday", "sunday", "satday"]})
days.pop(0)

for i, e in enumerate(days):
	if len(e.text.strip()) <= 2:
		x.append(int(e.text[0:1]))
	else:
		x.append(int(e.text[0:2]))
	# print(len(e.text))
	# print(e.text.strip())

pyplot.bar(x, y)
pyplot.show()