import os
import sys
import csv
import json
import random

import re
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

def doc2set(compilation, test_rate=0.2):
	url = 'data/{}/'.format(compilation)

	# Уравнять количество текстов из каждого документов

	max_count = min([len(file) for file in os.listdir(url) if '.json' in file])

	#

	files = [file for file in os.listdir(url) if '.json' in file]
	print(files)
	cont = []

	# ! Добавить разбиение документов на равные куски (100 слов)

	for name in files:
		category = name.split('.')[0]
		i = 0

		with open(url + name, 'r') as file:
			for string in file: # enumerate
				# Уравнять количество текстов из каждого документов

				if i == max_count:
					break

				#

				doc = json.loads(string)

				req = {
					'category': category,
					'cont': str2set(doc['cont']), # name
				}

				# Уравнивание документов

				if not 50 < len(req['cont']) < 300:
					continue

				#

				cont.append(req)
				i += 1

	random.shuffle(cont)
	categories = list(set([i['category'] for i in cont]))

	# Тестовая выборка

	count = int(len(cont) * test_rate)
	test = cont[:count]
	train = cont[count:]

	#

	return train, test, categories

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
			if freq[i] <= 2: # freq[i] > freq_max * 0.95 or freq[i] < freq_max * 0.2:
				corpus.remove(i)

	# Отсеивание частей речи



	# Стоп-слова

	if stop:
		stopwords = set(nltk.corpus.stopwords.words('russian'))
		stopwords = stopwords | {'это', 'россия', 'подпишись', 'подписаться', 'канал', 'youtube', 'instagram', 'фото', 'фотограффия', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь', 'наш', 'объясняем', 'объяснять', 'window', 'settings', 'components', 'eagleplayer', 'enabled', 'true', 'false', 'templates', 'multiplayer', 'relatedVideosHeight', 'ramblercommentscounter', 'relatedvideosheight', 'scroll', 'год', 'весь', 'также', 'лента', 'ру', 'х', 'р', 'т', 'д'}

		corpus = corpus - stopwords

	#

	return tuple(corpus)

def set2vector(data, corpus):
	return [int(j in data) for j in corpus]

def set2obj(data, corpus, categories):
	for i in range(len(data)):
		category_vec = [int(j == data[i]['category']) for j in categories]
		word_vec = set2vector(data[i]['cont'], corpus)

		data[i] = category_vec + word_vec

	return data

def obj2csv(vectors, corpus, categories):
	return [categories + ['"{}"'.format(el) for el in corpus]] + vectors

def vectorize(compilation, frequency):
	train, test, categories = doc2set(compilation)
	corpus = word_bag(train, frequency)

	vectors_train = set2obj(train, corpus, categories)
	vectors_test = set2obj(test, corpus, categories)

	csv_train = obj2csv(vectors_train, corpus, categories)
	csv_test = obj2csv(vectors_test, corpus, categories)

	return csv_train, csv_test, corpus, categories

def write(data, compilation, name, sign=','):
	name = 'data/{}/{}.csv'.format(compilation, name)

	# Для записи матриц
	if type(data) not in (list, tuple) or type(data[0]) not in (list, tuple):
		data = [data]

	with open(name, 'w') as file:
		for i in data:
			csv.writer(file, delimiter=sign, quotechar=' ', quoting=csv.QUOTE_MINIMAL).writerow(i)


if __name__ == '__main__':
	name = sys.argv[1]
	frequency = False if len(sys.argv) >= 3 else True

	train, test, corpus, categories = vectorize(name, frequency)

	write(train, name, 'train')
	write(test, name, 'test')
	write(corpus, name, 'corpus')
	write(categories, name, 'categories')

	# Отображение

	ds_train = len(train) - 1
	ds_test = len(test) - 1

	print('\nDataset: {} ({} + {})\nCorpus: {}\nCategories: {}\n{}\n'.format(ds_train+ds_test, ds_train, ds_test, len(corpus), len(categories), ' | '.join(categories)))