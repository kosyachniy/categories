from func import *
import codecs

delete('twits')

m=[]
with codecs.open('data/'+mas[ii][0]+'-news.txt', 'r', 'utf8') as file:
	for i in file:
		x=json.loads(i)['name']
		print(x)
		c=[int(j) for j in json.loads(i)['categories'].split()]
		write(c+text(x), name='twits', typ='a')