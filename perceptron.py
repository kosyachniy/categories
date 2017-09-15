from func import *
import numpy as np
#import random

act = lambda xe, we: sum([xe[i] * we[i] for i in range(len(xe))])

with open('data/table.csv', 'r') as f:
	x = np.loadtxt(f, delimiter=',', skiprows=1).T[countcat-1:].T
for i in range(len(x)):
	x[i][0] = 1

def neiro(column):
	print('Out №{}'.format(column))

	with open('data/table.csv', 'r') as f:
		y = np.loadtxt(f, delimiter=',', skiprows=1).T[column].T

	w = [0 for j in range(len(x[0]))] #random

	print(x)
	print(y)
	print(w)

	for iteration in range(27):
		print('Iteration №{}'.format(iteration+1))

		for i in range(len(x)):
			#Сделать ограничение на числа (ноль, бесконечность)
			error = y[i] - act(x[i], w)
			print(error)

			for j in range(len(x[i])):
				delta = x[i][j] * error
				print('Δw%d = %f' % (j, delta))
				w[j] += delta

			print('-----')

	return w

ai=[]
for i in range(countcat):
	ai.append(neiro(i))
ai=np.array(ai).T

np.savetxt('data/weights.csv', ai, delimiter=',')
print(ai)