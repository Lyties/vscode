import pandas as pd
import numpy as np

df = pd.read_csv('_01-data_analyse/pandas/test.csv')

print(df)

print('*' * 50)

t1 = pd.DataFrame(np.arange(12).reshape(3,4), index=list('abc'),columns=list('wxyz'))
print(t1)
print(t1.head(1))
print(t1.describe())
print(t1.info())

t1.sort_values(by='x')
print(t1)

# 前10行 DataFrame
print(t1[:10])
# 去一列 Series
print('*' * 2)
print(t1['x'])
# 区元素
print(t1.loc['a','w'])
print(t1.iloc[0,0])

print(t1.loc[['a'],:])
