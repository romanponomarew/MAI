#Импортировать NumPy под именем np
import numpy as np

#Напечатать версию и конфигурацию
#print(np.__version__)
#print(np.show_config())

#Создать вектор (одномерный массив) размера 10, заполненный нулями
# a = np.zeros(10)
#print(a)

#Создать вектор размера 10, заполненный единицами
# b = np.ones(10)
# #print(b)
#
# #Создать вектор размера 10, заполненный числом 2.5
# c = np.full(10, 2.5)
# #print(c)
#
# #Как получить документацию о функции numpy.add из командной строки?
# #python3 -c "import numpy; numpy.info(numpy.add)"
#
# #Создать вектор размера 10, заполненный нулями, но пятый элемент равен 1
# d = np.zeros(10)
# d[4] = 1
#print(d)

#Создать вектор со значениями от 10 до 49
# a = np.arange(10, 50, 1)
# print(a)

#Развернуть вектор (первый становится последним)
# a = np.arange(10, 50)
# # a = a[::-1]
# # print(a)

#Создать матрицу (двумерный массив) 3x3 со значениями от 0 до 8
# a = np.arange(9).reshape(3,3)
# print(a)

# a = np.array([[np.arange(4)], [np.arange(4, 7)], [np.arange(7, 10)]])
# print(a)

#Найти индексы ненулевых элементов в [1,2,0,0,4,0]
# a = np.nonzero([1, 2, 0, 0, 4, 0])
# print(a)

#Создать массив 3x3x3 со случайными значениями
# a = np.random.random((3, 3, 3))
# print(a)

# Создать массив 10x10 со случайными значениями, найти минимум и максимум
# a = np.random.random((10, 10))
# # min = a.min()
# # max = a.max()
#  print(min, max)

#Создать случайный вектор размера 30 и найти среднее значение всех элементов
# a = np.random.random(30)
# print(a)
# sr = a.mean()
# print(sr)

#Создать матрицу с 0 внутри, и 1 на границах
# a = np.ones((10, 10))
# a[1:-1, 1:-1] = 0
# print(a)


# Выяснить результат следующих выражений
#  (	0 * np.nan
#  	np.nan == np.nan
#  	np.inf > np.nan
#  	np.nan - np.nan)
0.3 == 3 * 0.1

#Создать 5x5 матрицу с 1,2,3,4 под диагональю
# a = np.diag(np.arange(1, 5), k=-1)
# print(a)

#Создать 8x8 матрицу и заполнить её в шахматном порядке
# a = np.zeros((8, 8), dtype=int)
# a[1::2, ::2] = 1
# a[::2, 1::2] = 1
# print(a)

#Дан массив размерности (6,7,8). Каков индекс (x,y,z) сотого элемента?
#print(np.unravel_index(100, (6, 7, 8)))

#Создать 8x8 матрицу и заполнить её в шахматном порядке, используя функцию tile
# a = np.tile(np.array([[0, 1], [1, 0]]), (4, 4))
# print(a)



