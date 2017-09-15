# Классификатор


№ | Тексты | Новости | Науки
---|---|---|---
1 | Наука | Политика | Математика
2 | Технологии | Технологии | Техника
3 | Новости | Происшествия | Физика
4 | Публицистика | Знаменитости | Химия
5 | Диалог | Спорт | Биология
6 | Юмор | Экономика | Программирование
7 | Информация | Наука | Филология
8 | Выражения |  | Иностранный язык

File -> Base -> Convert -> Perceptron -> Decide

```
python3 file.py
python3 base.py
python3 convert.py
python3 perceptron.py
python3 decide.py
```

1. Сделана проверка на плотность внутри предложения (убрать если будут маленькие предложения и заменить на выделение важных слов с помощью ИИ)
2. Сделать автозагрузку текстов и разбиение на предложение с установкой категорий
3. Разбить тексты на минимальные смысловые отрывки
4. На новый отрывок выводит определение, потом человек вбивает свой ответ и ответ сохраняется в базу обучения (или нет - если правильно определил ? - тестовая выборка)
