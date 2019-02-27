import os
import sys
import json
import random

import re
import numpy as np
# from pymystem3 import Mystem
from pymorphy2 import MorphAnalyzer
import nltk


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
					'cont': str2set(doc['name']), # cont
				})

	random.shuffle(cont)

	return cont

def word_bag(data, frequency=True, stop=True):
	corpus = set()

	for i in data:
		corpus = corpus | i['cont']

	# Частотное отсеивание

	if frequency:
		freq = {word: 0 for word in corpus}

		for el in data:
			for word in el['cont']:
				freq[word] += 1

		# ! Сделать по нормальному распределению

		counts = freq.values()
		freq_max = max(counts)

		print(freq)

		for i in freq:
			if freq[i] > freq_max * 0.8 or freq[i] < freq_max * 0.2:
				corpus.remove(i)

	# Стоп-слова

	if stop:
		stopwords = set(nltk.corpus.stopwords.words('russian'))
		stopwords = stopwords | {'это',}

		corpus = corpus - stopwords

	#

	return tuple(corpus)

def set2vector(data, corpus):
	return [int(j in data) for j in corpus]

def set2obj(data, corpus):
	categories = list(set(i['category'] for i in data))

	for i in range(len(data)):
		category_vec = [int(j == data[i]['category']) for j in categories]
		word_vec = set2vector(data[i]['cont'], corpus)

		data[i] = category_vec + word_vec

	return data, categories

def vectorize(compilation, frequency):
	cont = doc2set(compilation)
	corpus = word_bag(cont, frequency)
	vectors, categories = set2obj(cont, corpus)

	return vectors, corpus, categories

def write(data, compilation, name, sign=','):
	name = 'data/{}/{}.csv'.format(compilation, name)
	data = np.array(data)
	np.savetxt(name, data, delimiter=sign, fmt='%s')


if __name__ == '__main__':
	name = sys.argv[1]
	frequency = False if len(sys.argv) >= 3 else True

	vectors, corpus, categories = vectorize(name, frequency)

	vectors = [categories + ['"{}"'.format(el) for el in corpus]] + vectors

	write(vectors, name, 'train')
	write(corpus, name, 'corpus')
	write(categories, name, 'categories')

	print('\nDataset: {}\nCorpus: {}\nCategories: {}\n{}\n'.format(len(vectors), len(corpus), len(categories), ' | '.join(categories)))