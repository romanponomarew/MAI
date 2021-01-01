import numpy as np
import pandas as pd
#Постойте список уникальных типов самолетов зарегистрированных в России
aircraft = pd.read_csv('aircraft.csv', delimiter=';')
type = aircraft["Вид воздушного судна"] =="самолет"
aircrafts = aircraft.loc[type]
count = pd.Series(aircrafts["Тип (наименование) воздушного судна"].unique())
#print("Список уникальных самолетов, зарегистрированных в России: ", count)
#print("Список уникальных самолетов, зарегистрированных в России:" ,aircrafts["Тип (наименование) воздушного судна"].unique())

#Какой тип самолета имеет самую раннюю дату выдачи сертификата?
import datetime as dt
spisok_dat = aircraft["дата действующего свидетельства о регистрации"].values
#print(spisok_dat)
#print(spisok_dat[0])
min = dt.datetime.strptime(spisok_dat[0],'%d.%m.%Y')
#print("min1=", min)
count = 0
for val in spisok_dat:
    a = dt.datetime.strptime(val, '%d.%m.%Y')
    if a < min:
        min = a
        index = count
    count+=1
#print("min=", min, "index=", index)
aircraft_type = aircraft["Тип (наименование) воздушного судна"]
#print("Тип самолета с самой ранней датой выдачи сертификата -", aircraft_type[index])


#Построить запрос: Владелец Аэропорта, Аэропорт, Пассажиропоток суммарный за 2018, грузопоток суммарный за 2018

airports_df = pd.read_csv('airports(1).csv', delimiter=',', names =["НаименованиеаэропортаРФ", "Свидетельство о регистрации", "Владелец Аэропорта", "Тип аэропорта"])
passengers_df = pd.read_csv('passenger transportation(3).csv', delimiter=';')
cargo_df = pd.read_csv('cargo transportation(1).csv', delimiter=';')
#print(passengers_df.fillna(0))

#passenger transportation(3).csv:
passengers2018_df = passengers_df[passengers_df["Годпериодаданных"]==2018]
#print(passengers2018_df.loc[:,'Январь':'Сентябрь'].sum(axis=1))
sum_potok = passengers2018_df.loc[:,'Январь':'Сентябрь'].sum(axis=1)
#print(passengers2018_df)
pass_df = pd.DataFrame(passengers2018_df[["НаименованиеаэропортаРФ"]])
pass_df["Пассажиропоток"] = sum_potok #Dataframe Аэропорт+Сумм.пассажирпоток2018
#print(pass_df)

#airports(1).csv:
airports = airports_df[["НаименованиеаэропортаРФ", "Владелец Аэропорта"]]
#print(airports.merge(pass_df, how='right'))
airports = airports.merge(pass_df, how='right') #Аэропорт, Владелец Аэропорта, Суммарный поток
#print(airports)

#cargo transportation(1).csv:
cargo2018_df = cargo_df[cargo_df["Годпериодаданных"]==2018]
#print(cargo2018_df)
sum_cargo = cargo2018_df.loc[:,'Январь':'Сентябрь'].sum(axis=1)
#print(sum_cargo)
cargo = pd.DataFrame(cargo2018_df[["НаименованиеаэропортаРФ"]])
cargo["Грузопоток"] = sum_cargo #Dataframe Аэропорт+Сумм.пассажирпоток2018
#print(cargo)

#Finall:
#print(airports)
print(airports.merge(cargo, how = "left")) #Финальный результат: Аэропорт, Владелец Аэропорта, Суммарный поток, Пассажирпоток

#Перечислить аэропорты, где пассажиропоток меньше медианы, а грузопоток больше медианы:
final = airports.merge(cargo, how = "left")
print(final)

#zoo.water_need.median()
#sum_potok = passengers2018_df.loc[:,'Январь':'Сентябрь'].sum(axis=1)
# if (passengers2018_df.loc[:, 'Январь':'Сентябрь'].sum(axis=1)) != 0:
#     passengers2018_df["Медиана"] = passengers2018_df.loc[:, 'Январь':'Сентябрь'].median(axis=1)

#passengers2018_df["Медиана"] = passengers2018_df.loc[:, 'Январь':'Сентябрь'].median(axis=1)

medpas = passengers2018_df.loc[:, 'Январь':'Сентябрь'].median(axis=1)
print("med=", medpas)
med1 = pd.DataFrame(passengers2018_df)
med1["Пас.Медиана"] = medpas # Dataframe с столбцом медианы пассажиропотока 2018
print(med1)

#print(cargo2018_df.loc[:, 'Январь':'Сентябрь'])
medcargo = (cargo2018_df.loc[:, 'Январь':'Сентябрь']).median(axis=1)
med1["Груз.медиана"] = medcargo
print("ТАБ = ", med1)

med1 = med1.merge(final, how="left")
print(list(med1))

#Аэропорты, где пассажиропоток меньше медианы:
print(med1[med1["Пассажиропоток"]<med1["Пас.Медиана"]]) #0

#Аэропорты, где грузопоток больше медианы:
print(med1[med1["Грузопоток"]>med1["Груз.медиана"]][["НаименованиеаэропортаРФ","Грузопоток","Груз.медиана"]])







