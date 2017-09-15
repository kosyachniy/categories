from func import *

delete('table')
word=read(name='base')[0]
twit=read(name='twits')
write(['Теория', 'IT', 'Новости', 'Публицистика', 'Диалог', 'Юмор', 'Информация']+['"'+i+'"' for i in word], name='table')

twits=[]
for i in range(len(twit)):
	twits.append([int(l) for l in twit[i][0:7]])
	for j in word:
		twits[i].append(1) if j in twit[i] else twits[i].append(0)

for i in twits:
	write(i, name='table')