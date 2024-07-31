import pandas as pd

df = pd.read_csv('Top_100_Movies.csv')  # Читаем файл в переменную

# Вывод 5 строк дата-сета
print('\nПервые 5 первых строк дата-сета "Top_100_Movies.csv"')
print(df.head())

# Вывод описания колонок дата-сета
print('\nОписание колонок дата-сета "Top_100_Movies.csv"')
print(df.info())

# Вывод статистических данных по колонкам с числовыми данными
print('\nСтатистические данные по колонкам с числами дата-сета "Top_100_Movies.csv"')
print(df.describe())

# Расчёт средней з/платы по городам дата-сета dz.csv
print('\nCредняя зарплата по городам дата-сета "dz.csv"')
df2 = pd.read_csv('dz.csv')  # Читаем файл в переменную
group = df2.groupby('City')['Salary'].mean()
print(group)
