from funcvk import *
from decide import decide
import time

def hello(cont):
	cont=cont.lower()
	if any(i in cont for i in mess):
		return True
	return False

while True:
	for i in read():
		send(i[0], decide(i[1]))
	time.sleep(2)