#!/usr/bin/env python
# coding: utf-8

import requests
import pandas as pd

# Скачивание данных по ссылке:

url = 'https://testiws.ximad.com/export/events.csv.gz'
req = requests.get(url)
with open('events.csv.gz', "wb") as code:
    code.write(req.content)

del req    

# Загрузка скачанных по ссылке данных в таблицу:

events = pd.read_csv('events.csv.gz')


# Общая информация по данным:

#print(events.info())

#print(events.head())



# Для расчета метрики APRDAU нам необходимо агрегировать данные по дням, поэтому в поле 'event_time' оставим 
# только дату события без времени:

events['event_time'] = pd.to_datetime(events['event_time']).dt.normalize()


# Посчитаем выручку по дням:

revenue = events.groupby('event_time')['event_value'].sum()
#print(revenue)

# Посчитаем количество активных уникальных пользователей в день(DAU), исходя из значения поля 'event_name' равным 'launch' (запуск игры):

dau = events[events['event_name'] == 'launch'].groupby('event_time')['user_id'].nunique()
#print(dau)

# Посчитаем ARPDAU по всем дням:

arpdau = revenue / dau
print('ARPDAU: ', arpdau, sep='\n')

# График ARPDAU по дням:

#arpdau.plot(figsize=(10, 5), title = 'ARPDAU', grid=True)



# При необходимости сохраним файл в нужном формате, например в CSV:

arpdau.to_csv('arpdau_2021-09-07_2021-09-30.csv')



