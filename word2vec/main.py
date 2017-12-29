from func import *

categories = formed(('Технологии', 'Новости', 'Публицистика', 'Диалог', 'Юмор', 'Информация', 'Выражения', 'Наука'))

while True:
	x = formed(input().split())
	print(x)

	try:
		x = model.most_similar_to_given(x, categories)
	except:
		print('Ошибка рассчёта!')
	else:
		print(x.split('_')[0])