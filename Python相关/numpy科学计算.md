[TOC]


# array
```python
import numpy as np
ar = np.array([1, 2, 3, 4, 5, 6, 7])
print(ar)
print(ar.ndim)  # 数组维度个数（秩rank）
print(ar.shape)  # 数组维度
print(ar.size)  # 数组元素总数
print(ar.dtype)  # 数组中元素的类型
print(ar.itemsize)  # 数组中每个元素的字节大小
```

# 不同数据类型

```python
ar1 = np.array(range(10))  # 整型
ar2 = np.array([1, 2, 3.14, 4, 5])   # 浮点型
ar3 = np.array([[1, 2, 3], ('a', 'b', 'c')])   # 嵌套序列（列表，元祖均可）
ar4 = np.array([[1, 2, 3], ('a', 'b', 'c', 'd')]) 
print(ar1,type(ar1),ar1.dtype)
print(ar2,type(ar2),ar2.dtype)
print(ar3,ar3.shape,ar3.ndim,ar3.size)     # 二维数组，共6个元素
print(ar4,ar4.shape,ar4.ndim,ar4.size)     # 一维数组，共2个元素

print(np.arange(10))    # 返回0-9，整型
print(np.arange(10.0))  # 返回0.0-9.0，浮点型
print(np.arange(5,12))  # 返回5-11
print(np.arange(5.0,12,2))  # 返回5.0-12.0，步长为2
print(np.arange(10000))  # 如果数组太大而无法打印，NumPy会自动跳过数组的中心部分，并只打印边角
```

# linspace()
```python
ar1 = np.linspace(2.0, 3.0, num=5)
ar2 = np.linspace(2.0, 3.0, num=5, endpoint=False)
ar3 = np.linspace(2.0, 3.0, num=5, retstep=True)
print(ar1,type(ar1))
print(ar2)
print(ar3,type(ar3))
# linspace():返回在间隔[开始，停止]上计算的num个均匀间隔的样本。
# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# start：起始值，stop：结束值
# num：生成样本数，默认为50
# endpoint：如果为真，则停止是最后一个样本。否则，不包括在内。默认值为True。
# retstep：如果为真，返回（样本，步骤），其中步长是样本之间的间距 → 输出为一个包含2个元素的元祖，第一个元素为array，第二个为步长实际值
```

# zeros()
```python
ar1 = np.zeros(5)  
ar2 = np.zeros((2,2), dtype = np.int)
print(ar1,ar1.dtype)
print(ar2,ar2.dtype)
print('------')
# numpy.zeros(shape, dtype=float, order='C'):返回给定形状和类型的新数组，用零填充。
# shape：数组纬度，二维以上需要用()，且输入参数为整数
# dtype：数据类型，默认numpy.float64
# order：是否在存储器中以C或Fortran连续（按行或列方式）存储多维数据。
```

# 套用形状
```python
ar3 = np.array([list(range(5)),list(range(5,10))])
ar4 = np.zeros_like(ar3)
print(ar3)
print(ar4)
print('------')
# 返回具有与给定数组相同的形状和类型的零数组，这里ar4根据ar3的形状和dtype创建一个全0的数组
```

# ones
```python
ar5 = np.ones(9)
ar6 = np.ones((2,3,4))
ar7 = np.ones_like(ar3)
print(ar5)
print(ar6)
print(ar7)
# ones()/ones_like()和zeros()/zeros_like()一样，只是填充为1
```

# 单位矩阵
```python
print(np.eye(5))
# 创建一个正方的N*N的单位矩阵，对角线值为1，其余为0
```

# 一维数组索引及切片
```python
ar = np.arange(20)
print(ar)
print(ar[4])
print(ar[3:6])
```

# 二维数组索引及切片
```python
ar = np.arange(16).reshape(4,4)
print(ar, '数组轴数为%i' %ar.ndim)   # 4*4的数组
print(ar[2],  '数组轴数为%i' %ar[2].ndim)  # 切片为下一维度的一个元素，所以是一维数组
print(ar[2][1]) # 二次索引，得到一维数组中的一个值
print(ar[1:3],  '数组轴数为%i' %ar[1:3].ndim)  # 切片为两个一维数组组成的二维数组
print(ar[2,2])  # 切片数组中的第三行第三列 → 10
print(ar[:2,1:])  # 切片数组中的1,2行、2,3,4列 → 二维数组
print('-----')
```

# 三维数组索引及切片
```python
ar = np.arange(8).reshape(2,2,2)
print(ar, '数组轴数为%i' %ar.ndim)   # 2*2*2的数组
print(ar[0],  '数组轴数为%i' %ar[0].ndim)  # 三维数组的下一个维度的第一个元素 → 一个二维数组
print(ar[0][0],  '数组轴数为%i' %ar[0][0].ndim)  # 三维数组的下一个维度的第一个元素下的第一个元素 → 一个一维数组
print(ar[0][0][1],  '数组轴数为%i' %ar[0][0][1].ndim)  
```


# 布尔型索引：以布尔型的矩阵去做筛选
```python
ar = np.arange(12).reshape(3,4)
i = np.array([True,False,True])
j = np.array([True,True,False,False])
print(ar)
print(i)
print(j)
print(ar[i,:])  # 在第一维度做判断，只保留True，这里第一维度就是行，ar[i,:] = ar[i]（简单书写格式）
print(ar[:,j])  # 在第二维度做判断，这里如果ar[:,i]会有警告，因为i是3个元素，而ar在列上有4个
m = ar > 5
print(m)  # 这里m是一个判断矩阵
print(ar[m])  # 用m判断矩阵去筛选ar数组中>5的元素 → 重点！后面的pandas判断方式原理就来自此处

# 一个标量赋值给一个索引/切片时，会自动改变/传播原始数组
ar = np.arange(10)
print(ar)
ar[5] = 100
ar[7:9] = 200
print(ar)
```

# 复制
```python
ar = np.arange(10)
b = ar.copy()
b[7:9] = 200
print(ar)
print(b)
```

# 生成一个标准正态分布
```python
#numpy.random下的方法：
#normal(size=(4,4)) 标准正态分布
#rand(4,4) [0,1)的随机数
#randn 正态分布
#randint(size=(4,4)) 随机整数
samples = np.random.normal(size=(4,4))
print(samples)
```

# 均匀分布
```python
a = np.random.rand() # 生成一个随机浮点数
b = np.random.rand(4) # 生成形状为4的一维数组
c = np.random.rand(2,3) # 生成形状为2*3的二维数组，注意这里不是((2,3))

samples1 = np.random.rand(1000)
samples2 = np.random.rand(1000)
plt.scatter(samples1,samples2)
# 生成1000个均匀分布的样本值
```

# 正态分布

```python
samples1 = np.random.randn(1000)
samples2 = np.random.randn(1000)
plt.scatter(samples1,samples2)
# 生成1000个正太分布的样本值
```

# 生成范围内随机整数
```python
# numpy.random.randint(low, high=None, size=None, dtype='l')：生成一个整数或N维整数数组
# 若high不为None时，取[low,high)之间随机整数，否则取值[0,low)之间随机整数，且high必须大于low 
# dtype参数：只能是int类型  
print(np.random.randint(2))
# low=2：生成1个[0,2)之间随机整数  
print(np.random.randint(2,size=5))
# low=2,size=5 ：生成5个[0,2)之间随机整数
print(np.random.randint(2,6,size=5))
# low=2,high=6,size=5：生成5个[2,6)之间随机整数  
print(np.random.randint(2,size=(2,3)))
# low=2,size=(2,3)：生成一个2x3整数数组,取数范围：[0,2)随机整数 
print(np.random.randint(2,6,(2,3)))
# low=2,high=6,size=(2,3)：生成一个2*3整数数组,取值范围：[2,6)随机整数
```

# 随机种子
```python
# 计算机实现的随机数生成通常为伪随机数生成器，为了使得具备随机性的代码最终的结果可复现，需要设置相同的种子值
rng = np.random.RandomState(1)  
xtrain = 10 * rng.rand(30)
ytrain = 8 + 4 * xtrain + rng.rand(30)
# np.random.RandomState → 随机数种子，对于一个随机数发生器，只要该种子（seed）相同，产生的随机数序列就是相同的
# 生成随机数据x与y
# 样本关系：y = 8 + 4*x
fig = plt.figure(figsize =(12,3))
ax1 = fig.add_subplot(1,2,1)
plt.scatter(xtrain,ytrain,marker = '.',color = 'k')
plt.grid()
plt.title('样本数据散点图')
# 生成散点图
```

# 转置
```python
ar1 = np.arange(10)
ar2 = np.ones((5,2))
print(ar1,'\n',ar1.T)
print(ar2,'\n',ar2.T)
print('------')
# .T方法：转置，例如原shape为(3,4)/(2,3,4)，转置结果为(4,3)/(4,3,2) → 所以一维数组转置后结果不变
```

# 改变形状

```python
ar3 = ar1.reshape(2,5)     # 用法1：直接将已有数组改变形状             
ar4 = np.zeros((4,6)).reshape(3,8)   # 用法2：生成数组后直接改变形状
ar5 = np.reshape(np.arange(12),(3,4))   # 用法3：参数内添加数组，目标形状
print(ar1,'\n',ar3)
print(ar4)
print(ar5)
print('------')
# numpy.reshape(a, newshape, order='C')：为数组提供新形状，而不更改其数据，所以元素数量需要一致！！
```

# 改变形状并填充数据
```python
ar6 = np.resize(np.arange(5),(3,4))
print(ar6)
# numpy.resize(a, new_shape)：返回具有指定形状的新数组，如有必要可重复填充所需数量的元素。
# 注意了：.T/.reshape()/.resize()都是生成新的数组！！！
```
# 增加和减少维度
```python
a = np.array([1,2])
print(a.shape)  # (2,)
b = np.expand_dims(a, axis=1)
print(b.shape)  # (2,1)
c = np.squeeze(b, axis=1)
print(c.shape)  # (2,)
```

# 复制与赋值

```python
ar1 = np.arange(10)
ar2 = ar1
print(ar2 is ar1)
ar1[2] = 9
print(ar1,ar2)
# 回忆python的赋值逻辑：指向内存中生成的一个值 → 这里ar1和ar2指向同一个值，所以ar1改变，ar2一起改变
ar3 = ar1.copy()
print(ar3 is ar1)
ar1[0] = 9
print(ar1,ar3)
# copy方法生成数组及其数据的完整拷贝
# 再次提醒：.T/.reshape()/.resize()都是生成新的数组！！！
```

# 设置数组类型
```python
ar1 = np.arange(10,dtype=float)
print(ar1,ar1.dtype)
print('-----')
# 可以在参数位置设置数组类型
```

# 转换数据类型
```python
ar2 = ar1.astype(np.int32)
print(ar2,ar2.dtype)
print(ar1,ar1.dtype)
# a.astype()：转换数组类型
# 注意：养成好习惯，数组类型用np.int32，而不是直接int32
```

# 水平堆叠数据
```python
a = np.arange(5)    # a为一维数组，5个元素
b = np.arange(5,9) # b为一维数组,4个元素
ar1 = np.hstack((a,b))  # 注意:((a,b))，这里形状可以不一样
print(a,a.shape)
print(b,b.shape)
print(ar1,ar1.shape)
a = np.array([[1],[2],[3]])   # a为二维数组，3行1列
b = np.array([['a'],['b'],['c']])  # b为二维数组，3行1列
ar2 = np.hstack((a,b))  # 注意:((a,b))，这里形状必须一样
print(a,a.shape)
print(b,b.shape)
print(ar2,ar2.shape)
print('-----')
# numpy.hstack(tup)：水平（按列顺序）堆叠数组
```

# 垂直堆叠数据
```python
a = np.arange(5) 
b = np.arange(5,10)
ar1 = np.vstack((a,b))
print(a,a.shape)
print(b,b.shape)
print(ar1,ar1.shape)
a = np.array([[1],[2],[3]]) 
b = np.array([['a'],['b'],['c'],['d']]) 
ar2 = np.vstack((a,b))  # 这里形状可以不一样
print(a,a.shape)
print(b,b.shape)
print(ar2,ar2.shape)
print('-----')
# numpy.vstack(tup)：垂直（按列顺序）堆叠数组
```

# 沿着新轴连接数组的序列
```python
a = np.arange(5) 
b = np.arange(5,10)
ar1 = np.stack((a,b))
ar2 = np.stack((a,b),axis = 1)
print(a,a.shape)
print(b,b.shape)
print(ar1,ar1.shape)
print(ar2,ar2.shape)
# numpy.stack(arrays, axis=0)：沿着新轴连接数组的序列，形状必须一样！
# 重点解释axis参数的意思，假设两个数组[1 2 3]和[4 5 6]，shape均为(3,0)
# axis=0：[[1 2 3] [4 5 6]]，shape为(2,3)
# axis=1：[[1 4] [2 5] [3 6]]，shape为(3,2)
# 觉得还是直接使用vstack和hstack，以免出现维度混乱，影响后来的计算
```

# 按列拆分
```python
ar = np.arange(16).reshape(4,4)
ar1 = np.hsplit(ar,2)
print(ar)
print(ar1,type(ar1))
# numpy.hsplit(ary, indices_or_sections)：将数组水平（逐列）拆分为多个子数组 → 按列拆分
# 输出结果为列表，列表中元素为数组
```

# 按行拆
```python
ar2 = np.vsplit(ar,4)
print(ar2,type(ar2))
# numpy.vsplit(ary, indices_or_sections)：:将数组垂直（行方向）拆分为多个子数组 → 按行拆
```

# 与标量的运算

```python
ar = np.arange(6).reshape(2,3)
print(ar + 10)   # 加法
print(ar * 2)   # 乘法
print(1 / (ar+1))  # 除法
print(ar ** 0.5)  # 幂
```

# 各种统计值
```python
print(ar.mean())  # 求平均值
print(ar.max())  # 求最大值
print(ar.min())  # 求最小值
print(ar.std())  # 求标准差
print(ar.var())  # 求方差
print(ar.sum(), np.sum(ar,axis = 0))  # 求和，np.sum() → axis为0，按列求和；axis为1，按行求和
print(np.sort(np.array([1,4,3,2,5,6])))  # 排序
```