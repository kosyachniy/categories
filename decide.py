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

	m=sorted(result)[::-1]
	k=0
	tex=''
	print(m)
	while k<len(m) and m[k]>0:
		for i in range(7):
			if result[i]==m[k]:
				tex+=['Наука', 'Технологии', 'Новости', 'Публицистика', 'Диалог', 'Юмор', 'Информация'][i]+' ('+str(int(m[k]//10e115))+'%)\n'
		k+=1
	if not tex:
		tex='По этим данным невозможно определить категорию!'
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