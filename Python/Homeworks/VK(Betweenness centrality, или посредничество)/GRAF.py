import networkx as nx

# для визуализации
import matplotlib.pyplot as plt
#%config InlineBackend.figure_format = 'svg'
plt.rcParams['figure.figsize'] = (10, 6)
#Создание пустого графа
G = nx.Graph()
#Добавление узлов
G.add_nodes_from(["Маша", "Саша", "Cергей", "Даша", "Ваня","Таня", "Рома", "Кирилл", "Коля", "Вова", "Андрей", "Лена", "Света", "Лера"])
#G.nodes()
G.add_edge("Маша", "Саша")
G.add_edge("Cергей", "Саша")
G.add_edge("Даша", "Саша")
G.add_edge("Даша", "Cергей")
G.add_edge("Ваня", "Cергей")
G.add_edge("Ваня", "Маша")
G.add_edge("Коля", "Даша")
G.add_edge("Коля", "Лера")
G.add_edge("Лена", "Лера")
G.add_edge("Лена", "Рома")
G.add_edge("Маша", "Рома")
G.add_edge("Саша", "Рома")
G.add_edge("Лена", "Света")
G.add_edge("Сергей", "Лера")
G.add_edge("Даша", "Кирилл")
G.add_edge("Таня", "Маша")
G.add_edge("Вова", "Андрей")
G.add_edge("Андрей", "Саша")
G.add_edge("Таня", "Вова")
G.add_edge("Кирилл", "Рома")
G.add_edge("Сергей", "Кирилл")
G.add_edge("Таня", "Сергей")

nx.draw(G, with_labels=True, font_weight='bold')
plt.show();
print("Количество узлов в графе =", G.number_of_nodes())
print("Количество связей в графе =", G.number_of_edges())
bet_centr = nx.betweenness_centrality(G)
print(bet_centr)

for k,v in bet_centr.items():
    if v == max(bet_centr.values()):
        a = k
print(a)

