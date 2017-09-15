from func import *

word=[]
k=[]
for i in read(name='twits'):
	#word=[]
	for j in i[7:]:
		if j not in word:
			word.append(j)
			k.append(1)
		else:
			k[word.index(j)]+=1

	#Прибавление счётчика, только в новом предложении? Проверка не по количеству слов везде, а по плотности в одном примере
	#words=sorted(set(word), key=word.count, reverse=True)[:10]

print(len(k))
i=0
while i<len(k):
	if 3<=k[i]<=6: #Убирает слишком редкие и слишком частые, а также из списка нейтральных слов
		i+=1
	else:
		del k[i]
		del word[i]
print(len(k))


write(word, name='base', typ='w')