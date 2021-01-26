"""Тестовый файл для многопоточного(многоядерного) моделирования с имзмененными исходными данными"""
import random
import json
import asyncio
from time import time, sleep
import multiprocessing as mp



#Метод считывания графа из файла .json
with open("data(color)4.json", 'r', encoding='utf-8') as fh: #открываем файл на чтение
    graph = json.load(fh) #загружаем из файла данные в словарь graph
#print("GRAPH=", graph)


class Agent():
    """Класс для создания агента(каждого узла модели)"""
    def __init__(self, name):
        """Конструктор - изначальные аттрибуты агента при создании:"""
        self.name = name
        self.neighbors = []  # Список соседей агента
        self.val = graph["vars"][self.name]["initial"]  # Определение изначального цвета агента(задан в исходных данных)
        self.domen = graph["vars"][self.name]["domain"]  # Домен значений
        self.current_cycle = {}  # Состояние текущего цикла агента
        self.next_cycle = {}  # Состояние следующего цикла агента
        self.current_cost = 0  # Текущая стоимость(сумма штрафов) агента
        self.res = 0  # Результат работы всех циклов агента
        print(f"Агент {self.name} - создан")
        print(f"Значение агента ({self.name}) = ", self.val)

    def neighbor_search(self):
        """Определение списка соседей для текущего агента по исходным данным:"""
        for name in graph["pairs"]:
            if self.name == name[0]:
                self.neighbors.append(name[1])
            elif self.name == name[1]:
                self.neighbors.append(name[0])
        self.neighbors = list(set(self.neighbors))  # Оставляем только уникальные значения в списке
        print(f"Соседи агента {self.name} = ", self.neighbors)
        print()

    def send(self, agent):
        """Запись значения текущего агента переданному соседу(запись в его состояния циклов)"""
        if self.name in dict1[agent].neighbors: # Выполняем функцию только если соседи:
            print("------------")
            print(f"Агент {self.name} - сосед агента {agent}")
            print("Выполняем метод send")
            if self.name not in dict1[agent].current_cycle: #Есть ли значение текущего агента в текущем цикле соседа(i)
                print(f"Текущий Агент({self.name}) еще не отсылал свое значение агенту({dict1[agent].name})")
                dict1[agent].current_cycle[self.name] = self.val #Запись в словарь с ключом - имя текущего агента
                print(f"Текущий цикл агента({dict1[agent].name}) равен", dict1[agent].current_cycle) #Состояние текущего цикла соседа(i)
                if len(dict1[agent].neighbors) == len(dict1[agent].current_cycle): #Проверка на законченность цикла соседа
                    print(f"Цикл агента ({dict1[agent].name}) - завершен!")
                    # Расчет лучшего значения для переменной из цикла:
                    dict1[agent].evaluate_cycle(agent)

            else:   #Если текущий агент уже есть в текущем цикле соседа:
                print(f"Текущий Агент{self.name} уже отправлял значение агенту ({dict1[agent].name})")
                dict1[agent].next_cycle[self.name] = self.val #Запись значения текущего агента в следующий цикл соседа
                print(f"Поэтому записано в следующий цикла агента({dict1[agent].name}) = ", dict1[agent].next_cycle)
            print("------------")
            print()

    def func(self, val1, val2, name_neighbor):
        """Метод расчета стоимости между двумя значениями переменных агентов"""
        # global res1
        print("--------------")
        print(f"Выполняем метод func между ({self.name}) и ({name_neighbor})")
        res2 = 0
        for function in graph["functions"]:
            if (val1 == function[0] and val2 == function[1]) or (val1 == function[1] and val2 == function[2]):
                res2 = function[2]
        print(f"Значения текущего агента ({self.name})=({val1}), а значение агента ({name_neighbor})=({val2})")
        print(f"Поэтому штраф равен ", res2)
        print("--------------")
        print()
        return res2

    def evaluate_cycle(self, name):
        """Метод выбора наилучшего значения для переменной агента исходя из минимальной стоимости(выполняется в конце цикла)"""
        # dict1[name].current_cycle[dict1[name].name] = dict1[name].val
        print(f"Текущий цикл агента ({dict1[name].name}) = ", dict1[name].current_cycle)
        print("----------------")
        print(f"Выполняем метод расчета стоимости агента {name}")

        cost_otnosit = {}
        cost_current = 0
        for key, value in dict1[name].current_cycle.items():
            # Расчет стоимости агентом при текущем значении, суммируя стоимости со всеми соседями:
            print("Расчет стоимости при текущем значении")
            cost_current = cost_current + dict1[name].func(self.val, value, key)
        cost_otnosit[dict1[name].val] = cost_current
        print(f"Стоимость агента() при текущем значении ({dict1[name].val}) равна", cost_otnosit)

        # Создание словаря со стоимостью относительно состояния соседей, подставляя все значения из домена и суммируя их
        for args in dict1[name].domen:
            res1 = 0
            for key, value in dict1[name].current_cycle.items():
                res1 = res1 + dict1[name].func(args, value, key)
                cost_otnosit[args] = res1
            print("cost_otnosit=", cost_otnosit)

        # Выбор значения для переменной агента исходя из стоимостей
        val_min = 0
        for key, value in cost_otnosit.items():
            if value == min(cost_otnosit.values()):
                print(f"Минимальная стоимость агентом({dict1[name].name}) достигается при цвете", key)
                print(f"Значение агента({dict1[name].name}) меняем на", key)
                val_min = value
                dict1[name].val = key
                print(f"Текущий цвет агента({dict1[name].name})=", dict1[name].val)
                dict1[name].res = dict1[name].res + value  # Подсчет общей стоимости агента за всю работу модели
        global resulting_var
        resulting_var = resulting_var + val_min
        print(f"Прибавляем к финальной стоимости штраф цикла агента({dict1[name].name}) = ", val_min)
        print("Финальная стоимость на данный момент равна = ", resulting_var)
        cost_otnosit = {}
        dict1[name].current_cycle = {}  # Обнуляем текущий цикл:
        print("----------------")
        print()

def results():
    """Подсчет общей суммы штрафов всех агентов"""
    summa = 0
    for agent in graph["vars"].keys():
        summa = summa + dict1[agent].res
    for name in graph["vars"].keys():
        print(f"Цвет агента ({dict1[name].name}) - {dict1[name].val}")
    print("----------------------------------------------------")
    print("Общая стоимость модели(сумма всех штрафов) равна " + str(summa))
    print("Общий штраф по новому расчету равен ", resulting_var)


def init_agents():
    """Создание агентов по ключам графа"""
    global dict1
    for i in graph["vars"].keys():
        dict1[i] = Agent(i)
        dict1[i].neighbor_search()



#=======================MAIN==================#

if __name__ == '__main__':

    start = time()

    resulting_var = 0

    print("-------------------------------------------------------------------------")

    # Создание агентов по ключам графа
    dict1 = {}
    init_agents()

    procs = list()
    counts = 0
    for i in range(0, 1500):
        #procs = []
        for agent in graph["vars"].keys():
            # proc = mp.Process(target=dict1[agent].send(random.choice(list(graph["vars"].keys()))))
            if len(procs)<70:
                proc = mp.Process(target=dict1[agent].send(random.choice(list(graph["vars"].keys()))))
                procs.append(proc)
                counts = counts +1
                proc.start()
            if len(procs) == 69:
                for proc in procs:
                    proc.join()
                procs = []

            # else:
            #     # for proc in procs:
            #     #     proc.join()
            #         procs = []
    print("Кол-во процессов =", len(procs))
    # for proc in procs:
    #     proc.join()
    results()
    print("Кол-во действий равно ", counts)
    print(f"Script work time is {time() - start} s.")



