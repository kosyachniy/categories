from func import *
import codecs

delete('formated')

m=[]
with codecs.open('data/'+compilation+'/texts.txt', 'r', 'utf8') as file:
	for i in file:
		x=json.loads(i)['name']
		print(x)
		c=[int(j) for j in json.loads(i)['categories'].split()]
		write(c+text(x), name='formated', typ='a')