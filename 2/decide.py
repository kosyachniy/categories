from func import *
import math

def decide(cont):
	word=read(name='base')[0]
	ww=numread('weights').T

	cont=text(cont)

	result=[]
	for j in range(len(ww)):
		w=ww[j]
		k=0
		su=w[0]
		for i in cont:
			if i in word:
				k+=1
				su+=w[word.index(i)+1]

		su=round(su, 2) if k else 0
		result.append(su)

	###
	print(result)
	for i in range(len(result)):
		if math.isinf(result[i]):
			result[i]=0
	###

	m=max(result) #!!![:6]
	tex=''
	for i in range(7): #6 Почему часто выбирает последнее?
		if result[i]==m:
			tex+=['Наука', 'Технологии', 'Новости', 'Публицистика', 'Диалог', 'Юмор', 'Информация'][i]+'\n' #'Наука ({}%)'.format(su*100) if su>=0.5 else 'Наука ({}%)'.format((1-su)*100)) if su else 'По этим данным невозможно определить категорию!'
	#Убрать ответ, если сразу все категории
	#Почему бесконечность?
	#Убрать 0
	return tex

if __name__=='__main__':
	a=decide(input())
	print('==========')
	if a[0] in ('+','-'):
		print('CLOSE-OPEN')
	print(a,'\n==========')