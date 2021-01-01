# ==================
# ДЗ №1: простые типы данных, изменяемые и неизменяемые типы, работа со строками, списки

# Задание: сделайте анализ выгрузки квартир с ЦИАН:

# 1) Измените структуру данных, используемую для хранения данных о квартире. Сейчас квартира = список. Сделайте вместо этого квартира = словарь следующего вида: flat_info = {"id":flat[0], "rooms":flat[1], "type":flat[2], "price":flat[11]}. В задании используйте поля: идентификатор квартиры на ЦИАН, количество комнат, тип (новостройка или вторичка), стоимость

# 2) Подсчитайте количество новостроек, расположенных у каждого из метро

import csv

# читаем информацию о квартирах в список flats_list
flats_list = list()
with open('output.csv', encoding="utf-8") as csvfile:
	flats_csv = csv.reader(csvfile, delimiter=';')
	flats_list = list(flats_csv)

# убираем заголовок
header = flats_list.pop(0)

# создаем словарь с информацией о квартирах
subway_dict = {}
for flat in flats_list:
	subway = flat[3].replace("м.", "")
	subway_dict.setdefault(subway, [])
print(subway_dict)
# TODO 1: добавьте код, который генерирует новую структуру данных с информацией о квартире - словарь вместо списка
    # ваш код...
    # не забудьте сделать проверку типа и преобразовать то, что можно, в числа
for flat in flats_list:
    subway = flat[3].replace("м.", "")
    flat_info = {"id":flat[0], "rooms":flat[1], "type":flat[2], "price":flat[11]}
    if flat[0].isdigit() and flat[1].isdigit() and flat[11].isdigit():
        subway_dict.setdefault(subway, [])
        subway_dict[subway].append(flat_info)
print(subway_dict)
# TODO 2: подсчитайте и выведите на печать количество новостроек, расположенных рядом с каждым из метро. Используйте вариант прохода по словарю, который вам больше нравится
for key, value in subway_dict.items():
    n = 0
    if(key!=""):
        for v in value:

            for k, v1 in v.items():

                if (k=="type") and (v1=="новостройка"):
                    n += 1

        print(f"У метро {key}: {n} новостроек")
