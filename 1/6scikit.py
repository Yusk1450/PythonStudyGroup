
import numpy as np
from sklearn import svm
from sklearn.metrics import confusion_matrix

data = np.loadtxt('data.csv', delimiter=',')
y = data[:,0].astype(int)
x = data[:,1:3]

clf = svm.SVC(kernel='linear')
clf.fit(x, y)

data_test = np.loadtxt('data_test.csv', delimiter=',')
test_y = data[:,0].astype(int)
test_x = data[:,1:3]

print(test_y)
print(clf.predict(test_x))
# print(clf.score(test_x, test_y))