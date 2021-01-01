import pandas as pd
import numpy as np
df = pd.read_csv('group.tsv', sep='\t')
input_matrix = df.to_numpy()
output_matrix = np.zeros(input_matrix.shape[1]+3) #Задание нулевой строки для указания размера

def kontrol(element):
    b = element.split(",")
    c= np.array(b)
    kr = (np.count_nonzero(c =="+")*2.5 + np.count_nonzero(c =="+-")*2 + np.count_nonzero(c =="-+"))
    return kr

def rate(row):
    itog = 0
    propuski = np.count_nonzero(row == ".") +  np.count_nonzero(row == " ") + np.count_nonzero( row == "н")
    if propuski < 2:
        itog += 3
    c = kontrol(row[18])
    itog += c
    itog += (np.count_nonzero(row == "+")*2 - np.count_nonzero(row == "-") + np.count_nonzero(row == "+-"))
    row = np.append(row, itog) # первое значение
    row = np.append(row, round(itog)) # округлен
    if itog > 20:  # итог
        itog = 20
        row = np.append(row, 20)
    else:
        row = np.append(row, round(itog))
    global output_matrix
    output_matrix = np.vstack([output_matrix, row]) # складывание строк в матрицу

np.apply_along_axis(rate, 1, input_matrix)
output_matrix = np.delete(output_matrix, 0, 0) # Удаление первой, нулевой строки
print(output_matrix)

