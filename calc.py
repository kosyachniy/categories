from func import *

x=numread('table', 1).T
for i in range(len(x[0])):
	for j in range(7):
		x[j][i]=1
x=x[6:]
print(x)

y=numread('table', 1).T[0].T #0
print(y)

re=np.linalg.inv(x.dot(x.T)).dot(x)
w=re.dot(y)

np.savetxt('data/'+mas[ii][0]+'-weights.csv', w, delimiter=',')
print(w)