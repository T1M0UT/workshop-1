# TODO Planner

## Принцип роботи
Трекер одного конкретного плану - наприклад, ви поставили собі за мету пити воду 8 разів на день - кожен раз коли ви це робите - ви заходите в програму - обираєте що от ви це зараз зробили - і вона зараховує вам +1 з 8. Як тільки є 8 разів - дата цього дня додається в колонку “успішних” днів в csv-файл, якщо за день 8 разів не набирається і наступного разу ви заходите в програму вже наступного дня - день додається в колонку “неуспішних”. 

## Зберігання даних
![Зберігання даних](https://github.com/T1M0UT/workshop-1/blob/main/screen1.png)

## Використані модулі
```d
import datetime
import csv
import pandas
```
- #### Datetime для відображення дат
- #### csv для читання-запису Comma-Separated-Value файлів
- #### pandas для обрабки таблиць даних
