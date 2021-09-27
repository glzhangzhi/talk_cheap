```python
df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=['cobra', 'viper', 'sidewinder'],
     columns=['max_speed', 'shield'])
```
不推荐用迭代的方式更改数值
```python
for row in df.iterrows():
    print(row)  # 返回(Index, Series)对
    print(row[1])
    print(row[1][1])     

for row in df.itertuples():
    print(row)  # 返回[Index, A行值, A行值, ...]列表
    print(row[0])
    print(row[1])

for row in df.iteritems():
    print(row)  # 按列遍历，返回(行名，该行内容)对
    print(row[0])
    print(row[1])
    print(row[1][1])
```