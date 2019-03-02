import sys

import numpy as np
# from sklearn import preprocessing


FAULT = 0.01
EPOCHS_COUNT = 100
EPOCHS_DELTA = 0.999


def perceptron(name, outs, fault=FAULT):
	# Данные

	dataset = np.loadtxt('data/{}/train.csv'.format(name), delimiter=',', skiprows=1)

	x = np.hstack((np.ones((dataset.shape[0], 1)), dataset[:, outs:]))
	y = dataset[:, :outs]

	# Нормализация
	
	el = [i for i in x.reshape(1, -1)[0] if i>1]
	dis = int(max(np.log10(el))) + 1 if el else 1
	x = np.array([[j/10**dis for j in i] for i in x])

	# x = preprocessing.normalize(x)

	# Рассчёт весов

	def backpropagation(y):
		w = np.zeros((x.shape[1], 1))
		iteration = 0
		history = []

		while True: # for iteration in range(1, 51):
			iteration += 1
			error_max = 0

			for i in range(x.shape[0]):
				error = y[i] - x[i].dot(w).sum()

				error_max = max(error, error_max)
				# print('Error', error_max, error)

				for j in range(x.shape[1]):
					delta = x[i][j] * error
					w[j] += delta
					# print('Δw{} = {}'.format(j, delta))

			history.append(error_max)
			print('№{}: {}'.format(iteration, error_max)) #

			if error_max < fault or (iteration % 101 == 0 and error_max >= history[-EPOCHS_COUNT]*EPOCHS_DELTA):
				break

		return w

	w = np.hstack([backpropagation(i[:, 0]) for i in y.T.reshape(-1, y.shape[0], 1)])

	# Учёт нормализации
	
	w = np.array([[j/10**dis for j in i] for i in w])

	#

	return w

def test(compilation, outs, w):
	dataset = np.loadtxt('data/{}/test.csv'.format(compilation), delimiter=',', skiprows=1)
	x = np.hstack((np.ones((dataset.shape[0], 1)), dataset[:, outs:]))
	y = dataset[:, :outs]

	y = [np.where(row == 1.)[0][0] for row in y]
	result = [row.dot(w).argmax() == y[num] for num, row in enumerate(x)]

	return sum(result), len(result)


if __name__ == '__main__':
	compilation = sys.argv[1]
	outs = np.genfromtxt('data/{}/categories.csv'.format(compilation), delimiter=',').shape[0]
	fault = float(sys.argv[2]) if len(sys.argv) >= 3 else FAULT

	w = perceptron(compilation, outs, fault)

	# Сохранение весов

	print(w) #
	np.savetxt('data/{}/weights.csv'.format(compilation), w, delimiter=',')

	# Тестирование

	answ_right, answ_all = test(compilation, outs, w)
	print('Test: {}%'.format(answ_right * 100 // answ_all))