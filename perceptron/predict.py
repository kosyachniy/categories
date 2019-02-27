import numpy as np


def predict(x, compilation):
	# Обработка данных

	x = np.array([[1] + x])

	# Загрузка модели

	w = np.genfromtxt('data/{}/weights.csv'.format(compilation), delimiter=',')

	# Прогноз

	res = x.dot(w).sum(axis=0)

	return res.argmax()