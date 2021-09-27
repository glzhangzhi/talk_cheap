[TOC]

# 数据读写

```python
pd.read_csv()  # 的、读取csv文件
pd.read_excel()  # 读取表格
pd.read_sql()  # 读取数据库
df.to_csv()  # 写入csv
df.to_excel()  # 写入表格
df.to_sql()  # 写入数据库
```

# 数据概览

```python
df.head()  # 数据头部
df.tail()  # 数据尾部
df.shape()  # 数据行列数
df.columns()  # 数据列名
df.dtypes()  # 各变量类型
df.describe()  # 描述性统计量
S.value_counts()  # 序列对象的频次统计
```

# 数据清洗

```python
df.isnull  # 判断该数据是否为空
df.duplicated  # 数据是否存在重复值
df.dropna  # 删除缺失值
df.fillna  # 填充缺失值
df.drop_duplicated  # 删除重复值
df.drop  # 删除某变量或某行
```

# 类型转换及运算

```python
S.astype  # 类型转换
pd.to_datetime  # 转日期类型
S.map  # 元素级映射
S.apply  # 元素级处理
```


# Series 数据结构

Series 是带有标签的一维数组，可以保存任何数据类型（整数，字符串，浮点数，Python对象等）,轴标签统称为索引

## 查看数据、数据类型
```python
import numpy as np
import pandas as pd
s = pd.Series(np.random.rand(5))
print(s)
print(type(s))
```

## Series的相关属性
```python
print(s.index,type(s.index))
print(s.values,type(s.values))
# .index查看series索引，类型为rangeindex
# .values查看series值，类型是ndarray
```
核心：series相比于ndarray，是一个自带索引index的数组，即一维数组 + 对应索引，所以当只看series的值的时候，就是一个ndarray。series和ndarray较相似，索引切片功能差别不大。series和dict相比，series更像一个有顺序的字典（dict本身不存在顺序），其索引原理与字典相似（一个用key，一个用index）

# Series创建方法

## 由字典创建

字典的key就是index，values就是values
```python
dic = {'a':1 ,'b':2 , 'c':3, '4':4, '5':5}
s = pd.Series(dic)
print(s)
```
注意：key肯定是字符串，假如values类型不止一个会怎么样？ → dic = {'a':1 ,'b':'hello' , 'c':3, '4':4, '5':5}

## 由数组创建

```
arr = np.random.randn(5)
s = pd.Series(arr)
print(arr)
print(s)
# 默认index是从0开始，步长为1的数字

s = pd.Series(arr, index = ['a','b','c','d','e'],dtype = np.object)
print(s)
# index参数：设置index，长度保持一致
# dtype参数：设置数值类型
```

# Series 名称属性：name
```python
s1 = pd.Series(np.random.randn(5))
print(s1)
print('-----')
s2 = pd.Series(np.random.randn(5),name = 'test')
print(s2)
print(s1.name, s2.name,type(s2.name))
```
name为Series的一个参数，创建一个数组的 名称。
.name方法：输出数组的名称，输出格式为str，如果没用定义输出名称，输出为None

```python
s3 = s2.rename('hehehe')
print(s3)
print(s3.name, s2.name)
```
.rename()重命名一个数组的名称，并且新指向一个数组，原数组不变


# Dataframe 数据结构

Dataframe是一个表格型的数据结构，“带有标签的二维数组”。Dataframe带有index（行标签）和columns（列标签）

```python
data = {'name':['Jack','Tom','Mary'],
        'age':[18,19,20],
       'gender':['m','m','w']}
frame = pd.DataFrame(data)
print(frame)  
print(type(frame))
print(frame.index,'\n该数据类型为：',type(frame.index))
print(frame.columns,'\n该数据类型为：',type(frame.columns))
print(frame.values,'\n该数据类型为：',type(frame.values))
```
.index查看行标签
.columns查看列标签
.values查看值，数据类型为ndarray

# Dataframe创建方法

## 由数组或列表组成的字典
```python
data1 = {'a':[1,2,3],
        'b':[3,4,5],
        'c':[5,6,7]}
data2 = {'one':np.random.rand(3),
        'two':np.random.rand(3)}  
print(data1)
print(data2)
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print(df1)
print(df2)
```
由数组/list组成的字典 创建Dataframe，columns为字典key，index为默认数字标签
字典的值的长度必须保持一致！

```python
df1 = pd.DataFrame(data1, columns = ['b','c','a','d'])
print(df1)
df1 = pd.DataFrame(data1, columns = ['b','c'])
print(df1)
```
columns参数：可以重新指定列的顺序，格式为list，如果现有数据中没有该列（比如'd'），则产生NaN值
在columns重新指定的时候，列的数量可以少于原数据

```python
df2 = pd.DataFrame(data2, index = ['f1','f2','f3'])
print(df2)
```
index参数：重新定义index，格式为list，长度必须保持一致

## 由Series组成的字典
```python
data1 = {'one':pd.Series(np.random.rand(2)),
        'two':pd.Series(np.random.rand(3))}  # 没有设置index的Series
data2 = {'one':pd.Series(np.random.rand(2), index = ['a','b']),
        'two':pd.Series(np.random.rand(3),index = ['a','b','c'])}  # 设置了index的Series
print(data1)
print(data2)
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print(df1)
print(df2)
```
由Seris组成的字典 创建Dataframe，columns为字典key，index为Series的标签（如果Series没有指定标签，则是默认数字标签）
Series可以长度不一样，生成的Dataframe会出现NaN值


## 通过二维数组直接创建
```python
ar = np.random.rand(9).reshape(3,3)
print(ar)
df1 = pd.DataFrame(ar)
df2 = pd.DataFrame(ar, index = ['a', 'b', 'c'], columns = ['one','two','three'])  
print(df1)
print(df2)
```
通过二维数组直接创建Dataframe，得到一样形状的结果数据，如果不指定index和columns，两者均返回默认数字格式
index和colunms指定长度与原数组保持一致


# 切片

## 选择行
```python
df = pd.DataFrame(np.random.rand(12).reshape(3,4)*100,
                   index = ['one','two','three'],
                   columns = ['a','b','c','d'])
print(df)

data1 = df['a']
data2 = df[['a','c']]
print(data1,type(data1))
print(data2,type(data2))
print('-----')
```
按照列名选择列，只选择一列输出Series，选择多列输出Dataframe

```python
data3 = df.loc['one']
data4 = df.loc[['one','two']]
print(data3,type(data3))
print(data4,type(data4))
# 按照index选择行，只选择一行输出Series，选择多行输出Dataframe
```

## df[] - 选择列
一般用于选择列，也可以选择行，但不推荐，行索引用.loc与.iloc

```python
df = pd.DataFrame(np.random.rand(12).reshape(3,4)*100,
                   index = ['one','two','three'],
                   columns = ['a','b','c','d'])
print(df)
print('-----')

data1 = df['a']
data2 = df[['b','c']]  # 尝试输入 data2 = df[['b','c','e']]
print(data1)
print(data2)
```
df[]默认选择列，[]中写列名（所以一般数据colunms都会单独制定，不会用默认数字列名，以免和index冲突）
单选列为Series，print结果为Series格式
多选列为Dataframe，print结果为Dataframe格式

核心笔记：df[col]一般用于选择列，[]中写列名

## df.loc[] - 按index选择行
```python
df1 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                   index = ['one','two','three','four'],
                   columns = ['a','b','c','d'])
df2 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                   columns = ['a','b','c','d'])
print(df1)
print(df2)
print('-----')

data1 = df1.loc['one']
data2 = df2.loc[1]
print(data1)
print(data2)
print('单标签索引\n-----')
# 单个标签索引，返回Series

data3 = df1.loc[['two','three','five']]
data4 = df2.loc[[3,2,1]]
print(data3)
print(data4)
print('多标签索引\n-----')
# 多个标签索引，如果标签不存在，则返回NaN
# 顺序可变
# 这里‘five’标签不存在，所以有警告

data5 = df1.loc['one':'three']
data6 = df2.loc[1:3]
print(data5)
print(data6)
print('切片索引')
# 可以做切片对象
# 末端包含
```
核心笔记：df.loc[label]主要针对index选择行，同时支持指定index，及默认数字index

## iloc索引

```python
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                   index = ['one','two','three','four'],
                   columns = ['a','b','c','d'])
print(df)
print('------')

print(df.iloc[0])
print(df.iloc[-1])
#print(df.iloc[4])
print('单位置索引\n-----')
# 单位置索引
# 和loc索引不同，不能索引超出数据行数的整数位置

print(df.iloc[[0,2]])
print(df.iloc[[3,2,1]])
print('多位置索引\n-----')
# 多位置索引
# 顺序可变

print(df.iloc[1:3])
print(df.iloc[::2])
print('切片索引')
# 切片索引
# 末端不包含
```

## 布尔型索引
```python
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                   index = ['one','two','three','four'],
                   columns = ['a','b','c','d'])
print(df)
print('------')

b1 = df < 20
print(b1,type(b1))
print(df[b1])  # 也可以书写为 df[df < 20]
print('------')
# 不做索引则会对数据每个值进行判断
# 索引结果保留 所有数据：True返回原数据，False返回值为NaN

b2 = df['a'] > 50
print(b2,type(b2))
print(df[b2])  # 也可以书写为 df[df['a'] > 50]
print('------')
# 单列做判断
# 索引结果保留 单列判断为True的行数据，包括其他列

b3 = df[['a','b']] > 50
print(b3,type(b3))
print(df[b3])  # 也可以书写为 df[df[['a','b']] > 50]
print('------')
# 多列做判断
# 索引结果保留 所有数据：True返回原数据，False返回值为NaN
# 注意这里报错的话，更新一下pandas → conda update pandas

b4 = df.loc[['one','three']] < 50
print(b4,type(b4))
print(df[b4])  # 也可以书写为 df[df.loc[['one','three']] < 50]
print('------')
# 多行做判断
# 索引结果保留 所有数据：True返回原数据，False返回值为NaN

# 多重索引：比如同时索引行和列
# 先选择列再选择行 —— 相当于对于一个数据，先筛选字段，再选择数据量
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                   index = ['one','two','three','four'],
                   columns = ['a','b','c','d'])
print(df)
print('------')

print(df['a'].loc[['one','three']])   # 选择a列的one，three行
print(df[['b','c','d']].iloc[::2])   # 选择b，c，d列的one，three行
print(df[df['a'] < 50].iloc[:2])   # 选择满足判断索引的前两行数据
```

# 数据查看、转置

```python
df = pd.DataFrame(np.random.rand(16).reshape(8,2)*100,
                   columns = ['a','b'])
print(df.head(2))
print(df.tail())
# .head()查看头部数据
# .tail()查看尾部数据 默认查看5条

print(df.T)
# .T 转置
```


# 添加与修改
```python
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                   columns = ['a','b','c','d'])
print(df)

df['e'] = 10
df.loc[4] = 20
print(df)
# 新增列/行并赋值

df['e'] = 20
df[['a','c']] = 100
print(df)
# 索引后直接修改值
```

# 删除  del / drop()
```python
df = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                   columns = ['a','b','c','d'])
print(df)

del df['a']
print(df)
print('-----')
# del语句 - 删除列

print(df.drop(0))
print(df.drop([1,2]))
print(df)
print('-----')
# drop()删除行，inplace=False → 删除后生成新的数据，不改变原数据

print(df.drop(['d'], axis = 1))
print(df)
# drop()删除列，需要加上axis = 1，inplace=False → 删除后生成新的数据，不改变原数据
```

# 对齐
```python
df1 = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])
print(df1 + df2)
# DataFrame对象之间的数据自动按照列和索引（行标签）对齐
```

# 排序1 - 按值排序 .sort_values

同样适用于Series
```python
df1 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                   columns = ['a','b','c','d'])
print(df1)
print(df1.sort_values(['a'], ascending = True))  # 升序
print(df1.sort_values(['a'], ascending = False))  # 降序
print('------')
# ascending参数：设置升序降序，默认升序
# 单列排序

df2 = pd.DataFrame({'a':[1,1,1,1,2,2,2,2],
                  'b':list(range(8)),
                  'c':list(range(8,0,-1))})
print(df2)
print(df2.sort_values(['a','c']))
# 多列排序，按列顺序排序
# 注意inplace参数
```

# 排序2 - 索引排序 .sort_index
```python
df1 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                  index = [5,4,3,2],
                   columns = ['a','b','c','d'])
df2 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                  index = ['h','s','x','g'],
                   columns = ['a','b','c','d'])
print(df1)
print(df1.sort_index())
print(df2)
print(df2.sort_index())
# 按照index排序
# 默认 ascending=True, inplace=False
```

# 均值mean

```python
df = pd.DataFrame({'key1':[4,5,3,np.nan,2],
                 'key2':[1,2,np.nan,4,5],
                 'key3':[1,2,3,'j','k']},
                 index = ['a','b','c','d','e'])
print(df)
print(df['key1'].dtype,df['key2'].dtype,df['key3'].dtype)
print('-----')

m1 = df.mean()
print(m1,type(m1))
print('单独统计一列:',df['key2'].mean())
print('-----')
# np.nan ：空值
# .mean()计算均值
# 只统计数字列
# 可以通过索引单独统计一列

m2 = df.mean(axis=1)
print(m2)
print('-----')
# axis参数：默认为0，以列来计算，axis=1，以行来计算，这里就按照行来汇总了

m3 = df.mean(skipna=False)
print(m3)
print('-----')
# skipna参数：是否忽略NaN，默认True，如False，有NaN的列统计结果仍未NaN
```

# 主要数学计算方法

可用于Series和DataFrame（1）
```python
df = pd.DataFrame({'key1':np.arange(10),
                  'key2':np.random.rand(10)*10})
print(df)
print('-----')

print(df.count(),'→ count统计非Na值的数量\n')
print(df.min(),'→ min统计最小值\n',df['key2'].max(),'→ max统计最大值\n')
print(df.quantile(q=0.75),'→ quantile统计分位数，参数q确定位置\n')
print(df.sum(),'→ sum求和\n')
print(df.mean(),'→ mean求平均值\n')
print(df.median(),'→ median求算数中位数，50%分位数\n')
print(df.std(),'\n',df.var(),'→ std,var分别求标准差，方差\n')
print(df.skew(),'→ skew样本的偏度\n')
print(df.kurt(),'→ kurt样本的峰度\n')

df['key1_s'] = df['key1'].cumsum()
df['key2_s'] = df['key2'].cumsum()
print(df,'→ cumsum样本的累计和\n')

df['key1_p'] = df['key1'].cumprod()
df['key2_p'] = df['key2'].cumprod()
print(df,'→ cumprod样本的累计积\n')

print(df.cummax(),'\n',df.cummin(),'→ cummax,cummin分别求累计最大值，累计最小值\n')
# 会填充key1，和key2的值
```

# 唯一值：.unique()
```python
s = pd.Series(list('asdvasdcfgg'))
sq = s.unique()
print(s)
print(sq,type(sq))
print(pd.Series(sq))
# 得到一个唯一值数组
# 通过pd.Series重新变成新的Series

sq.sort()
print(sq)
# 重新排序
```


# 值计数：.value_counts()
```python
sc = s.value_counts(sort = False)  
# 也可以这样写：pd.value_counts(sc, sort = False)
print(sc)
# 得到一个新的Series，计算出不同值出现的频率
# sort参数：排序，默认为True
```

# 成员资格：.isin()
```python
s = pd.Series(np.arange(10,15))
df = pd.DataFrame({'key1':list('asdcbvasd'),
                  'key2':np.arange(4,13)})
print(s)
print(df)
print('-----')

print(s.isin([5,14]))  # 元素5和14是否在s中
print(df.isin(['a','bc','10',8]))
# 用[]表示
# 得到一个布尔值的Series或者Dataframe
```


# 通过str访问，且自动排除丢失/ NA值
```python
s = pd.Series(['A','b','C','bbhello','123',np.nan,'hj'])
df = pd.DataFrame({'key1':list('abcdef'),
                  'key2':['hee','fv','w','hija','123',np.nan]})
print(s)
print(df)
print('-----')

print(s.str.count('b'))
print(df['key2'].str.upper())
print('-----')
# 直接通过.str调用字符串方法
# 可以对Series、Dataframe使用
# 自动过滤NaN值

df.columns = df.columns.str.upper()  # 将df的列名改成大写
print(df)
# df.columns是一个Index对象，也可使用.str
```

# 字符串常用方法（1） - lower，upper，len，startswith，endswith
```python
s = pd.Series(['A','b','bbhello','123',np.nan])

print(s.str.lower(),'→ lower小写\n')
print(s.str.upper(),'→ upper大写\n')
print(s.str.len(),'→ len字符长度\n')
print(s.str.startswith('b'),'→ 判断起始是否为a\n')
print(s.str.endswith('3'),'→ 判断结束是否为3\n')
```

# 字符串常用方法（2） - strip
```python
s = pd.Series([' jack', 'jill ', ' jesse ', 'frank'])
df = pd.DataFrame(np.random.randn(3, 2), columns=[' Column A ', ' Column B '], index=range(3))
print(s)
print(df)
print('-----')

print(s.str.strip())  # 去除字符串中的空格，指前后空格
print(s.str.lstrip())  # 去除字符串中的左空格
print(s.str.rstrip())  # 去除字符串中的右空格

df.columns = df.columns.str.strip()
print(df)
# 这里去掉了columns的前后空格，但没有去掉中间空格
```

# 字符串常用方法（3） - replace
```python
df = pd.DataFrame(np.random.randn(3, 2), columns=[' Column A ', ' Column B '],index=range(3))
df.columns = df.columns.str.replace(' ','-')
print(df)
# 替换

df.columns = df.columns.str.replace('-','hehe',n=1)
print(df)
# n：替换个数
```

# 字符串常用方法（4） - split、rsplit
```python
s = pd.Series(['a,b,c','1,2,3',['a,,,c'],np.nan])
print(s.str.split(','))
print('-----')
# 类似字符串的split

print(s.str.split(',')[0])
print('-----')
# 直接索引得到一个list

print(s.str.split(',').str[0])
print(s.str.split(',').str.get(1))
print('-----')
# 可以使用get或[]符号访问拆分列表中的元素

print(s.str.split(',', expand=True))
print(s.str.split(',', expand=True, n = 1))
print(s.str.rsplit(',', expand=True, n = 1))
print('-----')
# 可以使用expand可以轻松扩展此操作以返回DataFrame
# n参数限制分割数
# rsplit类似于split，反向工作，即从字符串的末尾到字符串的开头

df = pd.DataFrame({'key1':['a,b,c','1,2,3',[':,., ']],
                  'key2':['a-b-c','1-2-3',[':-.- ']]})
print(df['key2'].str.split('-'))
# Dataframe使用split

# 字符串索引
s = pd.Series(['A','b','C','bbhello','123',np.nan,'hj'])
df = pd.DataFrame({'key1':list('abcdef'),
                  'key2':['hee','fv','w','hija','123',np.nan]})

print(s.str[0])  # 取第一个字符串
print(s.str[:2])  # 取前两个字符串
print(df['key2'].str[0]) 
# str之后和字符串本身索引方式相同
```



# 改变维度

```python
df.values.reshape(1, -1)  #此时返回的为numpy.array对象 
```



# merge合并

```python
df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
df3 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                    'key2': ['K0', 'K1', 'K0', 'K1'],
                    'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3']})
df4 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                    'key2': ['K0', 'K0', 'K0', 'K0'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']})
print(pd.merge(df1, df2, on='key'))
print('------')
# left：第一个df
# right：第二个df
# on：参考键

print(pd.merge(df3, df4, on=['key1','key2']))
# 多个链接键

# 参数how → 合并方式
print(pd.merge(df3, df4,on=['key1','key2'], how = 'inner'))  
print('------')
# inner：默认，取交集

print(pd.merge(df3, df4, on=['key1','key2'], how = 'outer'))  
print('------')
# outer：取并集，数据缺失范围NaN

print(pd.merge(df3, df4, on=['key1','key2'], how = 'left'))  
print('------')
# left：按照df3为参考合并，数据缺失范围NaN

print(pd.merge(df3, df4, on=['key1','key2'], how = 'right'))  
# right：按照df4为参考合并，数据缺失范围NaN

# 参数 left_on, right_on, left_index, right_index → 当键不为一个列时，可以单独设置左键与右键
df1 = pd.DataFrame({'lkey':list('bbacaab'),
                   'data1':range(7)})
df2 = pd.DataFrame({'rkey':list('abd'),
                   'date2':range(3)})
print(pd.merge(df1, df2, left_on='lkey', right_on='rkey'))
print('------')
# df1以‘lkey’为键，df2以‘rkey’为键

df1 = pd.DataFrame({'key':list('abcdfeg'),
                   'data1':range(7)})
df2 = pd.DataFrame({'date2':range(100,105)},
                  index = list('abcde'))
print(pd.merge(df1, df2, left_on='key', right_index=True))
# df1以‘key’为键，df2以index为键
# left_index：为True时，第一个df以index为键，默认False
# right_index：为True时，第二个df以index为键，默认False

# 所以left_on, right_on, left_index, right_index可以相互组合：
# left_on + right_on, left_on + right_index, left_index + right_on, left_index + right_index
```

# 连接：concat
```python
s1 = pd.Series([1,2,3])
s2 = pd.Series([2,3,4])
print(pd.concat([s1,s2]))
print('-----')
# 默认axis=0，行+行

s3 = pd.Series([1,2,3],index = ['a','c','h'])
s4 = pd.Series([2,3,4],index = ['b','e','d'])
print(pd.concat([s3,s4]).sort_index())
print(pd.concat([s3,s4], axis=1))
print('-----')
# axis=1,列+列，成为一个Dataframe
# 更新的版本中将默认不排序，因此需要在concat方法中使用sort=True参数来启用排序
```

# 去重 .duplicated
```python
s = pd.Series([1,1,1,1,2,2,2,3,4,5,5,5,5])
print(s.duplicated())
print(s[s.duplicated() == False])
print('-----')
# 判断是否重复
# 通过布尔判断，得到不重复的值

s_re = s.drop_duplicates()
print(s_re)
print('-----')
# drop.duplicates移除重复
# inplace参数：是否替换原值，默认False

df = pd.DataFrame({'key1':['a','a',3,4,5],
                  'key2':['a','a','b','b','c']})
print(df.duplicated())
print(df['key2'].duplicated())
# Dataframe中使用duplicated

s = pd.Series(list('ascaazsd'))
print(s.replace('a', np.nan))
print(s.replace(['a','s'] ,np.nan))
print(s.replace({'a':'hello world!','s':123}))
# 可一次性替换一个值或多个值
# 可传入列表或字典
```

# 分组
```python
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})
print(df)
print('------')

print(df.groupby('A'), type(df.groupby('A')))
print('------')
# 直接分组得到一个groupby对象，是一个中间数据，没有进行计算

a = df.groupby('A').mean()
b = df.groupby(['A','B']).mean()
c = df.groupby(['A'])['D'].mean()  # 以A分组，算D的平均值
print(a,type(a),'\n',a.columns)
print(b,type(b),'\n',b.columns)
print(c,type(c))
# 通过分组后的计算，得到一个新的dataframe
# 默认axis = 0，以行来分组
# 可单个或多个（[]）列分组

df = pd.DataFrame({'X' : ['A', 'B', 'A', 'B'], 'Y' : [1, 4, 3, 2]})
print(df)
print(df.groupby('X'), type(df.groupby('X')))
print('-----')

print(list(df.groupby('X')), '→ 可迭代对象，直接生成list\n')
print(list(df.groupby('X'))[0], '→ 以元祖形式显示\n')
for n,g in df.groupby('X'):
    print(n)
    print(g)
    print('###')
print('-----')
# n是组名，g是分组后的Dataframe

print(df.groupby(['X']).get_group('A'),'\n')
print(df.groupby(['X']).get_group('B'),'\n')
print('-----')
# .get_group()提取分组后的组

grouped = df.groupby(['X'])
print(grouped.groups)
print(grouped.groups['A'])  # 也可写：df.groupby('X').groups['A']
print('-----')
# .groups：将分组后的groups转为dict
# 可以字典索引方法来查看groups里的元素

sz = grouped.size()
print(sz,type(sz))
print('-----')
# .size()：查看分组后的长度

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})
grouped = df.groupby(['A','B']).groups
print(df)
print(grouped)
print(grouped[('foo', 'three')])
# 按照两个列进行分组

s = pd.Series([1, 2, 3, 10, 20, 30], index = [1, 2, 3, 1, 2, 3])
grouped = s.groupby(level=0)  # 唯一索引用.groupby(level=0)，将同一个index的分为一组
print(grouped)
print(grouped.first(),'→ first：非NaN的第一个值\n')
print(grouped.last(),'→ last：非NaN的最后一个值\n')
print(grouped.sum(),'→ sum：非NaN的和\n')
print(grouped.mean(),'→ mean：非NaN的平均值\n')
print(grouped.median(),'→ median：非NaN的算术中位数\n')
print(grouped.count(),'→ count：非NaN的值\n')
print(grouped.min(),'→ min、max：非NaN的最小值、最大值\n')
print(grouped.std(),'→ std，var：非NaN的标准差和方差\n')
print(grouped.prod(),'→ prod：非NaN的积\n')

df = pd.DataFrame({'a':[1,1,2,2],
                  'b':np.random.rand(4),
                  'c':np.random.rand(4),
                  'd':np.random.rand(4),})
print(df)
print(df.groupby('a').agg(['mean',np.sum]))
print(df.groupby('a')['b'].agg({'result1':np.mean,
                               'result2':np.sum}))
# 函数写法可以用str，或者np.方法
# 可以通过list，dict传入，当用dict时，key名为columns → 更新pandas后会出现警告
# 尽量用list传入
```

# 读取普通分隔数据

```python
# 读取普通分隔数据：read_table
# 可以读取txt，csv

import os
os.chdir('C:/Users/iHJX_Alienware/Desktop/')

data1 = pd.read_table('data1.txt', delimiter=',',header = 0, index_col=1)
print(data1)
# delimiter：用于拆分的字符，也可以用sep：sep = ','
# header：用做列名的序号，默认为0（第一行）
# index_col：指定某列为行索引，否则自动索引0, 1, .....

# read_table主要用于读取简单的数据，txt/csv

# 读取csv数据：read_csv
# 先熟悉一下excel怎么导出csv

data2 = pd.read_csv('data2.csv',encoding = 'utf-8')
print(data2.head())
# encoding：指定字符集类型，即编码，通常指定为'utf-8'

# 大多数情况先将excel导出csv，再读取
```

# 读取excel数据

```python
# 读取excel数据：read_excel

data3 = pd.read_excel('地市级党委书记数据库（2000-10）.xlsx',sheet_name='中国人民共和国地市级党委书记数据库（2000-10）',header=0)
print(data3.head())
# io ：文件路径。
# sheetname：返回多表使用sheetname=[0,1],若sheetname=None是返回全表 → ① int/string 返回的是dataframe ②而none和list返回的是dict
# header：指定列名行，默认0，即取第一行
# index_col：指定列为索引列，也可以使用u”strings”
```

# 可视化
```python
df.plot('Country', [7, 8, 9, 10], kind='bar')  # 柱状图
df.plot('Country', [7, 8, 9, 10], kind='line')  # 线状图
df.plot('Country', [7, 8, 9, 10], kind='box')  # 箱型图
df.plot('Country', [7, 8, 9, 10], kind='scatter')  # 散点图
df.plot('Country', [7, 8, 9, 10], kind='bar', xlim=(0, 20), ylim=(0, 100))  # 设置轴取值范围
df[:20][‘Freedom’].plot(kind=’line’,xlim=(0,20),ylim=(0,100),color=’red’,xticks=([0,10,15,20]),yticks=([0,50,70,100]), title = ‘xticks’)  # 自定义坐标轴数字
```