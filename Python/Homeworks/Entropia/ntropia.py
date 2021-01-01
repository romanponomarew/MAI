import math
import csv
students_list = list()
with open('output.csv', encoding="utf-8") as csvfile:
	students_csv = csv.reader(csvfile, delimiter=';')
	students_list = list(students_csv)

header = students_list.pop(0)
print(header)
print(students_list)
#print(students_list[0])   #студент
#print(students_list[0][1]) #редактор студента

redaktor = list()
for stroka in students_list:
    redaktor.append(stroka[1])
#print(redaktor) # Список со значениями признака редактора для всех студентов
redak = set(redaktor) #Множество с неповторяющимися редакторами
#print(redak)
spisok = list()
for i in redak:
    p = redaktor.count(i) / len(redaktor) #Частота значения
    m = p * math.log(p) #Энтропия для одного значения
    spisok.append(m) #Список с энтропиями значений
print(spisok)
#entropia = sum(spisok)
print(sum(spisok)) #Общая энтропия для признака

