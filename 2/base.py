from func import *

word=[]
k=[]
for i in read(name='twits'):
	for j in range(7, len(i[:-1])):
		for l in range(7, len(i[:-1])):
			if i[j]!=i[j+1] and i[j]+'-'+i[j+1] not in word and i[j+1]+'-'+i[j] not in word:
				word.append(i[j]+'-'+i[j+1])

write(word, name='base', typ='w')