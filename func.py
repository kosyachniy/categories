import requests, json, csv, re, time, vk_api, math
from parse import parse
import numpy as np

get=lambda src: requests.get(src).text

compilation=str(1)

with open('data/'+compilation+'/set.txt') as file:
	j = json.loads(file.read())
	categories = j['categories']
	countcat = len(categories)
	vk = vk_api.VkApi(token = j['token'])
	vk.auth()

# Работа с файлами
def delete(name):
	with open('data/'+compilation+'/'+name+'.csv', 'w') as file:
		pass

def write(text, name, typ='a', sign=','):
	if len(text):
		with open('data/'+compilation+'/'+name+'.csv', typ) as file:
			csv.writer(file, delimiter=sign, quotechar=' ', quoting=csv.QUOTE_MINIMAL).writerow(text)

def read(name, sign=','):
	with open('data/'+compilation+'/'+name+'.csv', 'r') as file:
		return [i for i in csv.reader(file, delimiter=sign, quotechar=' ')]

def numread(name, nom=0):
	with open('data/'+compilation+'/'+name+'.csv', 'r') as f:
		return np.loadtxt(f, delimiter=',', skiprows=nom)

def text(x):
	y = []
	for i in parse(x):
		for j in i.word:
			if j['speech'] in ('noun', 'adjf', 'verb'):
				y.append(j['infinitive'])
	return y

#ВКонтакте
send = lambda user, cont: vk.method('messages.send', {'user_id':user, 'message':cont})

def readvk():
	cont = []
	for i in vk.method('messages.get')['items']:
		if not i['read_state']:
			cont.append([i['user_id'], i['body']])
	return cont[::-1]