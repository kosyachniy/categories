import sys
import time
import csv
import numpy as np

from func.vk_group import read, send
from scikit.predict import predict
from vectorize import str2set, set2vector
# from vector.main import vector


def csv_read(category, name, sign=','):
	with open('data/{}/{}.csv'.format(category, name), 'r') as file:
		return [i[0] for i in csv.reader(file, delimiter=sign, quotechar=' ')]

# def pretty(x):
# 	if x:
# 		return '%s (%d%%)' % (cats[x[0]], x[1] * 100 if x[1] < 1 else 99)
# 	else:
# 		return 'По этим данным невозможно определить категорию!'


if __name__ == '__main__':
	name = sys.argv[1]

	categories = csv_read(name, 'categories')

	print(categories)

	while True:
		# try:
		for i in read():
			print(i)
			corpus = csv_read(name, 'corpus')
			vec = set2vector(str2set(i[1]), corpus)
			res = predict(vec, name)
			print(res, categories)
			send(i[0], categories[res])

			# z2 = pretty(vector(i[1]))
			# if z2:
			# 	send(i[1], 'Google: ' + z2)
		time.sleep(2)
		# except:
		# 	time.sleep(5)
		# 	#vk.auth()