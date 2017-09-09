import numpy as np
#import random

act = lambda xe, we: sum([xe[i] * we[i] for i in range(len(xe))])

with open('data/text-table.csv', 'r') as f:
	x = np.loadtxt(f, delimiter=',', skiprows=1).T
with open('data/text-table.csv', 'r') as f:
	y = np.loadtxt(f, delimiter=',', skiprows=1).T[0].T

for i in range(len(x[0])):
	for j in range(7):
		x[j][i] = 1
x = x[6:]
x = x.T
w = [0 for j in range(len(x[0]))] #random

print(x)
print(y)
print(w)

for iteration in range(27):
	print('Iteration №{}'.format(iteration+1))

	for i in range(len(x)):
		#Сделать ограничение на числа (ноль, бесконечность)
		error = (y[i] - act(x[i], w))

		for j in range(len(x[i])):
			print('Δw%d = %f' % (j, x[i][j] * error))
			w[j] += x[i][j] * error

		print('-----')

np.savetxt('data/text-weights.csv', w, delimiter=',')
print(w)