import sys
import time
import csv

from func.vk_group import read, send
from vectorize import str2set, set2vector
from perceptron.predict import predict as per_pred
from scikit.predict import predict as sci_pred
# from vector.main import vector


def csv_read(category, name, sign=','):
	with open('data/{}/{}.csv'.format(category, name), 'r') as file:
		return [i for i in csv.reader(file, delimiter=sign, quotechar=' ')][0]

# def pretty(x):
# 	if x:
# 		return '%s (%d%%)' % (cats[x[0]], x[1] * 100 if x[1] < 1 else 99)
# 	else:
# 		return 'По этим данным невозможно определить категорию!'


if __name__ == '__main__':
	name = sys.argv[1]

	categories = csv_read(name, 'categories')

	print(categories) #

	while True:
		try:
			for i in read():
				print(i)

				corpus = csv_read(name, 'corpus')
				vec = set2vector(str2set(i[1]), corpus)

				# ! Выводить список значимых слов
				# print(vec)

				sci_res = sci_pred(vec, name)
				per_res = per_pred(vec, name)

				print(sci_res, per_res)

				send(i[0], 'SciKit: {}\nПерцептрон: {}'.format(categories[sci_res], categories[per_res]))

				# z2 = pretty(vector(i[1]))
				# if z2:
				# 	send(i[1], 'Google: ' + z2)
			time.sleep(2)
		except:
			time.sleep(5)
			#vk.auth()