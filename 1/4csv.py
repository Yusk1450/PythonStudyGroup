
from matplotlib import pyplot
import csv

def getData():
	rows = []
	f = open('ranks.csv', 'r')
	reader = csv.reader(f)
	for row in reader:
		rows.append(row)
	f.close()
	return rows

rows = getData()
rows.pop(0)

xs = []
ys = []
for i in range(len(rows)):
	x = rows[i][1]					# グリーンカレー
	y = rows[i][2]					# 杏仁豆腐
	if len(x) == 0 or len(y) == 0:
		continue
	xs.append(x)
	ys.append(y)

print(xs)
print(ys)

pyplot.xlim(0, 6)
pyplot.ylim(0, 6)

pyplot.plot(xs, ys, 'o')
pyplot.show()
