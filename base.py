from func import *

words=[] #set()
k=[]
for i in read(name='twits'):
	word=[]
	for j in i[7:]:
		if j not in word:
			word.append(j)

		'''
		 #add(j)
#
			k.append(1)
		else:
			k[word.index(j)]+=1
		'''

	#Проверка не по количеству слов везде, а по алотности в одном примере
	words=sorted(set(word), key=word.count, reverse=True)[:10]

'''
print(len(k))
i=0
while i<len(k):
	if k[i]<=4 or word[i] in ('тот', 'какой', 'один', 'самый', 'год', 'быть', 'такой', 'который', 'фото'): #or word[i] in ('',)
		del k[i]
		del word[i]
	else:
		i+=1
print(len(k))
#Убирать слишком частые слова и слишком редкие (?)
'''

write(word, name='base', typ='w')