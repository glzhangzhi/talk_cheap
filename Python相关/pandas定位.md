# loc
```python
df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=['cobra', 'viper', 'sidewinder'],
     columns=['max_speed', 'shield'])
     
df.loc['viper']  # 获取一行
df.loc[['viper', 'sidewinder']]  # 获取多行
df.loc['cobra', 'shield']  # 获取一行的一列
df.loc['cobra':'viper', 'max_speed']  # 获取多行的一列
df.loc[['viper', 'sidewinder'], ['shield']] = 50  # 赋值多行的一列
df.loc['cobra'] = 10  # 赋值一行的多列

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=[7, 8, 9], columns=['max_speed', 'shield'])

df.loc[7:9]  # 获取整型作为index的多行
```

# iloc
```python
mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 }]
df = pd.DataFrame(mydict)

df.iloc[0]  # 获取一行，返回Series
df.iloc[[0]]  # 获取一行，返回Dataframe
df.iloc[[0, 1]]  # 获取多行
df.iloc[:3]  # 多行切片
df.iloc[0, 1]  # 获取某行某列
df.iloc[[0, 2], [1, 3]]  # 获取多行多列
df.iloc[1:3, 0:3]  # 多行多列切片
```
# at
```python
df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
                  index=[4, 5, 6], columns=['A', 'B', 'C'])
                  
df.at[4, 'B']  # 获取某行某列
df.at[4, 'B'] = 10  # 赋值某行某列
df.loc[5].at['B']  # loc获取某行，at获取某列
```