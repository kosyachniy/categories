from func import *

categories = formed(('Технологии', 'Новости', 'Публицистика', 'Диалог', 'Юмор', 'Информация', 'Выражения', 'Наука', 'Рецепты', 'Происшествие', 'Событие', 'Афиша'))

def vector(x):
	try:
		y = model.most_similar_to_given(x, categories)
	except:
		try:
			x = model.most_similar_cosmul(positive=x)
			print(x)
			y = model.most_similar_to_given(x[0][0], categories)
		except:
			print('По этим данным невозможно определить категорию!')
		else:
			print(y.split('_')[0], model.distance(x[0][0], y))
	else:
		print(y.split('_')[0], model.distance(x, y))

if __name__ == '__main__':
	while True:
		x = formed(input().split())
		print(x)

		print(vector(x))