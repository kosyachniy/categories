from func import *

#fault = 0.997 #с какой погрешностью нужен ответ

act = lambda xe, we: sum([xe[i] * we[i] for i in range(len(xe))])

with open('data/' + compilation + '/table.csv', 'r') as f:
	x = np.loadtxt(f, delimiter=',', skiprows=1).T[countcat-1:].T
for i in range(len(x)):
	x[i][0] = 1

#Уменьшаем разряд параметров, чтобы при обучении нейронов не выходили громадные ошибки (с каждым разом увеличиваясь)
discharge = 0
for i in x:
	for j in i[1:]:
		print(j)
		dis = int(math.log(j, 10)) + 1 if j != 0 else 0 #если =1 не добавлять разряд
		if dis > discharge:
			discharge = dis

for i in range(len(x)):
	for j in range(1, len(x[0])):
		x[i][j] /= 10 ** discharge

def neiro(column):
	print('Out №{}'.format(column))

	with open('data/' + compilation + '/table.csv', 'r') as f:
		y = np.loadtxt(f, delimiter=',', skiprows=1).T[column].T

	w = [0 for j in range(len(x[0]))]

	print(x)
	print(y)
	print(w)

	start = True
	fault = 0
	iteration = 0
	while True: #for iteration in range(1, 47):
		iteration += 1
		print('iteration №{}'.format(iteration))

		err = 0

		for i in range(len(x)):
			error = y[i] - act(x[i], w)
			#print(error)

			if error > err: err = error

			for j in range(len(x[i])):
				delta = x[i][j] * error
				#print('Δw%d = %f' % (j, delta))
				w[j] += delta

			#print('-----')

		print('ошибка: %f (%f)' % (err, fault))
		if start:
			fault = err
			start = False
		else:
			if err >= fault: #Остаться рядом с локальным минимумом
				print('exit')
				break
			fault = err

	return w

w = []
for i in range(countcat):
	w.append([j / (10 ** discharge) for j in neiro(i)])
	w[len(w)-1][0] *= 10 ** discharge
w = np.array(w).T

#Сохранение весов
np.savetxt('data/' + compilation + '/weights.csv', w, delimiter=',')
print(w)