import os
import sys
import json
# import csv
import random

import re
import numpy as np
# from pymystem3 import Mystem
from pymorphy2 import MorphAnalyzer


# def lemmatize(text):
# 	processed = Mystem().analyze(text)
# 	lemma = lambda word: word['analysis'][0]['lex'].lower().strip()
# 	return set(lemma(word) for word in processed if 'analysis' in word)

def lemmatize(text):
	m = MorphAnalyzer()
	lemma = lambda word: m.parse(word)[0].normal_form
	return set(lemma(word) for word in text.split())

def str2set(text):
	text = re.sub(r'[^a-zA-Zа-яА-Я]', ' ', text)
	return lemmatize(text)

def doc2set(compilation):
	url = 'data/{}/'.format(compilation)
	files = [file for file in os.listdir(url) if '.json' in file]
	cont = []

	for name in files:
		category = name.split('.')[0]

		with open(url + name, 'r') as file:
			for string in file:
				doc = json.loads(string)

				cont.append({
					'category': category,
					'cont': str2set(doc['cont']),
				})

	random.shuffle(cont)

	return cont

def word_bag(texts):
	corpus = set()

	for i in texts:
		corpus = corpus | i['cont']

	# Стоп-слова
	# Частотное отсеивание

	return tuple(corpus)

def set2vector(data, corpus):
	categories = list(set(i['category'] for i in data))

	for i in range(len(data)):
		category_vec = [int(j == data[i]['category']) for j in categories]
		word_vec = [int(j in data[i]['cont']) for j in corpus]

		data[i] = category_vec + word_vec

	return data, categories

def vectorize(name):
	cont = doc2set(name)
	corpus = word_bag(cont)
	vectors, categories = set2vector(cont, corpus)

	return vectors, corpus, categories

# def write(text, compilation, name, sign=','):
# 	with open('data/{}/{}.csv'.format(compilation, name), 'w') as file:
# 		if type(text[0]) == list:
# 			for el in text:
# 				csv.writer(file, delimiter=sign, quotechar=' ', quoting=csv.QUOTE_MINIMAL).writerow(el)
# 		else:
# 			csv.writer(file, delimiter=sign, quotechar=' ', quoting=csv.QUOTE_MINIMAL).writerow(text)

def write(data, compilation, name, sign=','):
	name = 'data/{}/{}.csv'.format(compilation, name)
	data = np.array(data)
	np.savetxt(name, data, delimiter=sign, fmt='%s')


if __name__ == '__main__':
	name = sys.argv[1]

	vectors, corpus, categories = vectorize(name)

	vectors = [categories + ['"{}"'.format(el) for el in corpus]] + vectors

	write(vectors, name, 'train')
	write(corpus, name, 'corpus')
	write(categories, name, 'categories')

	print('\nDataset: {}\nCorpus: {}\nCategories: {}\n{}\n'.format(len(vectors), len(corpus), len(categories), ' | '.join(categories)))