import sys

import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
import joblib


OUTS = 1


def logistic_regression(name, outs=OUTS):
	# Данные

	dataset = np.loadtxt('data/{}/train.csv'.format(name), delimiter=',', skiprows=1)

	x = dataset[:, outs:]
	y = dataset[:, :outs]

	# Стандартизация

	x = preprocessing.normalize(x)

	# Рассчёт весов

	model = []
	for i in range(outs):
		model.append(LogisticRegression())
		model[-1].fit(x, y[:, i])

	#

	return model


if __name__ == '__main__':
	name = sys.argv[1]
	outs = int(sys.argv[2]) if len(sys.argv) >= 3 else OUTS

	model = logistic_regression(name, outs)

	# Сохранение модели

	for i, el in enumerate(model):
		# print(el)
		joblib.dump(el, 'data/{}/model-{}.txt'.format(name, i))