import numpy as np
import pandas as pd
metro = pd.read_csv('METRO(3).csv', delimiter=';')
print(metro,"\n")

coffee = metro[metro["coffee"]!=0]
#print(coffee)
print("Станции на которых пьют кофе:")
print(coffee[["name", "coffee", "tea" ]], "\n")

tea = metro[metro["tea"]!=0]
#print(tea)
print("Станции на которых пьют чай:")
print(tea[["name", "tea", "coffee"]])