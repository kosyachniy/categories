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

	print(result)

	m=sorted(result)[::-1]
	tex=''
	try:
		raz=int(math.log(m[0], 10))-1
	except:
		print('Error!')
	else:
		k=0
		while k<len(m) and m[k]>0:
			for i in range(7):
				if result[i]==m[k]:
					tex+=['Наука', 'Технологии', 'Новости', 'Публицистика', 'Диалог', 'Юмор', 'Информация'][i]+' ('+str(int(m[k]//(10**raz)))+'%)\n'
			k+=1

	return tex if len(tex) else 'По этим данным невозможно определить категорию!'

if __name__=='__main__':
	print(decide(input()))