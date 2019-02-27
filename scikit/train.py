import sys

import numpy as np
# from sklearn import preprocessing
# from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib


OUTS = 1


def logistic_regression(name, outs=OUTS):
	# Данные

	dataset = np.loadtxt('data/{}/train.csv'.format(name), delimiter=',', skiprows=1)

	x = dataset[:, outs:]
	y = dataset[:, :outs]

	# Преобразование y

	y = [list(row).index(1) for row in y]

	# Стандартизация

	# x = preprocessing.normalize(x)

	# Рассчёт весов

	# sc = StandardScaler()
	# sc.fit(x)
	# x_std = sc.transform(x)
	# x_test_std = sc.transform(x_test)
	x_std = x
	# x_test_std = x_test

	model = LogisticRegression(C=1000.0, random_state=0)
	model.fit(x_std, y)

	#

	return model


if __name__ == '__main__':
	name = sys.argv[1]
	outs = int(sys.argv[2]) if len(sys.argv) >= 3 else OUTS

	model = logistic_regression(name, outs)

	# Сохранение модели

	# print(model)
	joblib.dump(model, 'data/{}/model.txt'.format(name))