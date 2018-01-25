from perceptron.decide import decide
from vector.main import vector

import time, json

with open('data/set.txt', 'r') as file:
	cats = json.loads(file.read())['categories']

#ВКонтакте
import vk_api

with open('data/keys.txt', 'r') as file:
	vk = vk_api.VkApi(token=json.loads(file.read())['token'])
vk.auth()

send = lambda user, cont: vk.method('messages.send', {'user_id':user, 'message':cont})
readvk = lambda: [[i['user_id'], i['body']] for i in vk.method('messages.get')['items'] if not i['read_state']][::-1]

pretty = lambda x: '%s (%d%%)' % (cats[x[0]], x[1] * 100 if x[1] < 1 else 99) if x else 'По этим данным невозможно определить категорию!'

while True:
	try:
		for i in readvk():
			z1 = decide(i[1])
			z2 = vector(i[1])

			text = ''
			if z1[1] > 0.1:
				text = pretty(z1) + '\n'
			if z2:
				text += 'Google: %s' % pretty(z2)
			if not z1 and not z2:
				text = 'По этим данным невозможно определить категорию!'

			send(i[0], text)
		time.sleep(2)
	except:
		time.sleep(5)
		vk.auth()