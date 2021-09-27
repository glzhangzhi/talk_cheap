今天找到一个进度条的库tqdm

https://github.com/tqdm/tqdm#usage

主要解决的问题是，在python程序中会使用大量的for循环，使用这个库套用上for的迭代器，会自动计算剩余循环百分比，并显示进度条，还有需要许多参数可以对进度条进行自定义。

这里主要介绍两种使用方法

 # 1.基于迭代器的
```python
from tqdm import tqdm
import time

text = ''
for char in tqdm(['a', 'b', 'c', 'd']):
	time.sleep(0.25)
	text = text + char
```
或者可以使用trange(i)代替tqdm(range(i))
```python
pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    time.sleep(0.25)
    pbar.set_description("Processing %s" % char)
```
使用tqdm建立的迭代器设置描述，可以表示正在处理的迭代对象

# 2.手动控制
```python
with tqdm(total=100) as pbar:
	for i in range(10):
		time.sleep(0.1)
		pbar.update(10)
```
这里手动实例化进度条对象，并且在每一次迭代以后手动更新进度条
作者在这里推荐使用with，这样方便在使用完成以后清除内存占用
也可以使用 pbar = tqdm(total=100) 的方式建立，但是记得在使用完成以后pbar.del()或者tqdm.close()删除占用
