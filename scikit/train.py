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

def test(compilation, outs, model):
	dataset = np.loadtxt('data/{}/test.csv'.format(compilation), delimiter=',', skiprows=1)
	x = dataset[:, outs:]
	y = dataset[:, :outs]

	y = [np.where(row == 1.)[0][0] for row in y]
	result = [model.predict([row])[0] == y[num] for num, row in enumerate(x)]

	return sum(result), len(result)


if __name__ == '__main__':
	compilation = sys.argv[1]
	outs = np.genfromtxt('data/{}/categories.csv'.format(compilation), delimiter=',').shape[0]

	model = logistic_regression(compilation, outs)

	# Сохранение модели

	joblib.dump(model, 'data/{}/model.txt'.format(compilation))
	# print(model)

	# Тестирование

	answ_right, answ_all = test(compilation, outs, model)
	print('Test: {}%'.format(answ_right * 100 // answ_all))