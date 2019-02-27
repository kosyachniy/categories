import joblib


def predict(x, compilation):
	# Обработка данных

	x = [x] # [[1] + x]

	# Загрузка модели

	model = joblib.load('data/{}/model.txt'.format(compilation))

	# Прогноз

	res = model.predict(x)[0] # _proba

	return res