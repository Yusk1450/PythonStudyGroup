
from operator import itemgetter
from math import sqrt
import csv

def getData():
	rows = []
	f = open('ranks.csv', 'r')
	reader = csv.reader(f)
	for row in reader:
		rows.append(row)
	f.close()
	return rows

def getSimDistance(data1, data2):
	items1 = []
	items2 = []
	for i in range(len(data1)):
		e1 = data1[i]
		e2 = data2[i]
		if len(e1) == 0 or len(e2) == 0:
			continue
		items1.append(float(e1))
		items2.append(float(e2))

	# ひとつも共通項がなかったら...
	if len(items1) == 0:
		return 0

	sum = 0
	for i in range(len(items1)):
		sum += pow(items1[i] - items2[i], 2)

	return 1/(1+sqrt(sum))


rows = getData()
rows.pop(0)

idx = 0					# 山田さん
user = rows[idx]
print(user[0], 'との類似度')
user.pop(0)

sims = {}
for i, e in enumerate(rows):
	if i == idx:
		continue
	name = e[0]
	e.pop(0)
	sims[name] = getSimDistance(user, e)

# print(sims)
print(sorted(sims.items(), key=itemgetter(1), reverse=True))