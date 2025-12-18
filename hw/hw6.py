#Pandas — это библиотека Python для работы с данными.
#Pandas нужен, чтобы быстро и удобно анализировать и обрабатывать данные, вместо ручной работы со списками и словарями.
import pandas as pd
a = ['red', 'green', 'blue', 'white']
df = pd.Series(a, index = ['x', 'y', 'z', 'k'])
print(df)

data = {'cities' : ['Osh', 'Istanbul', 'New-York'], 'capitals' : ['Bishkek', 'Tashkent', 'Ankara']}
df = pd.DataFrame(data)
print(df)

print(df.loc[0])

