from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout
from keras.utils.np_utils import to_categorical
from keras.optimizers import Adagrad
from keras.optimizers import Adam
import numpy as np
from PIL import Image
import os

image_list = []
label_list = []

# トレーニングデータを読み込む
for dir in os.listdir("data/train"):

	traindir = "data/train/" + dir
	if os.path.isdir(traindir) == False:
		continue

	label = 0				# 正解ラベル

	if dir == "apple":
		label = 0			# りんごの場合は、0
	elif dir == "orange":
		label = 1			# オレンジの場合は、1

	for file in os.listdir(traindir):
		if file != ".DS_Store":

			label_list.append(label)			# 正解ラベルを配列に入れる

			filepath = traindir + "/" + file	# ファイルパス

			resized_img = Image.open(filepath).resize((25, 25))													# 画像を25x25にリサイズする
			image = np.array(resized_img)																		# 25x25の2次元配列にする→[[R,G,B], [R,G,B]...]
			image = image.transpose(2, 0, 1)																	# 配列を次元を変換する→[[R,R,R,...], [G,G,G,...], [B,B,B,...]]
			image = image.reshape(1, image.shape[0] * image.shape[1] * image.shape[2]).astype("float32")[0]		# 1次元配列に変換→[R,R,R,...,G,G,G,...,B,B,B]
			image_list.append(image / 255.)															# 0.0〜1.0までの値にして配列に入れる

image_list = np.array(image_list)		# 画像リストをnumpy配列に変換

Y = to_categorical(label_list)			# 正解ラベルを配列にする（0→[1,0], 1→[0,1]）

# 層を構築
model = Sequential()
# 入力層
model.add(Dense(200, input_dim=1875))
model.add(Activation("relu"))
model.add(Dropout(0.2))

# 隠れ層
model.add(Dense(200))
model.add(Activation("relu"))
model.add(Dropout(0.2))

# 出力層
model.add(Dense(2))
model.add(Activation("softmax"))

# オプティマイザにAdamを使用
opt = Adam(lr=0.001)
model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])
# nb_epoch: 学習回数
# batch_size: 1度に処理する分量（GPUモードの際は、メモリ制限がある場合がある）
# model.fit(image_list, Y, nb_epoch=1500, batch_size=100, validation_split=0.1)
model.fit(image_list, Y, nb_epoch=10, batch_size=100, validation_split=0.1)

total = 0.
ok_count = 0.

for dir in os.listdir("data/test"):
	
	testdir = "data/test/" + dir
	if os.path.isdir(testdir) == False:
		continue

	label = 0

	if dir == "apple":
		label = 0			# りんごの場合は、0
	elif dir == "orange":
		label = 1			# オレンジの場合は、1

	for file in os.listdir(testdir):
		if file != ".DS_Store":
			label_list.append(label)
			filepath = testdir + "/" + file

			resized_img = Image.open(filepath).resize((25, 25))	
			image = np.array(resized_img)
			image = image.transpose(2, 0, 1)
			image = image.reshape(1, image.shape[0] * image.shape[1] * image.shape[2]).astype("float32")[0]

			# 予測する
			print(filepath)
			result = model.predict_classes(np.array([image / 255.]))
			print("label:", label, "result:", result[0])

			total += 1.

			if label == result[0]:
				ok_count += 1.

print(ok_count / total * 100, "%")