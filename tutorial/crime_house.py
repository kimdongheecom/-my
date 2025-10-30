
import pandas as pd

house = pd.read_csv('house.csv')
print(house)
print(house.head())
print(house.tail())
print(house.info())
print(house.describe())
print(house.columns)
print(house.index)
print(house.values)
print(house.shape)
print(house.size)
print(house.dtypes)
print(house.ndim)
print(house.nunique())
print(house.describe())