import vk_api, json

with open('set.txt', 'r') as file:
	vk=vk_api.VkApi(token=json.loads(file.read())['token'])
vk.auth()

send=lambda user, cont: vk.method('messages.send', {'user_id':user, 'message':cont})

def readvk():
	cont=[]
	for i in vk.method('messages.get')['items']:
		if not i['read_state']:
			cont.append([i['user_id'], i['body']])
	return cont[::-1]