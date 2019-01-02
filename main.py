from func.vk_group import *
from perceptron.decide import decide
from vector.main import vector

import time
import json


with open('data/sets.json', 'r') as file:
	cats = json.loads(file.read())['categories']

def pretty(x):
	if x:
		return '%s (%d%%)' % (cats[x[0]], x[1] * 100 if x[1] < 1 else 99)
	else:
		return 'По этим данным невозможно определить категорию!'


if __name__ == '__main__':
	while True:
		try:
			for i in read():
				send(i[0], decide(i[1]))

				z2 = pretty(vector(i[1]))
				if z2:
					send(i[1], 'Google: ' + z2)
			time.sleep(2)
		except:
			time.sleep(5)
			#vk.auth()