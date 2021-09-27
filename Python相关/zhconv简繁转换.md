最近找到一个轻量级的简繁转换库

https://github.com/gumblex/zhconv

安装
pip install zhconv

使用
简体转繁体
```python
zhconv.convert('计算机软件', 'zh-tw')
>>>計算機軟體
```
繁体转简体
```python
zhconv.convert('計算機軟體', 'zh-cn')
>>>计算机软件
```
繁体转简体（逐字转换）
```python
zhconv.convert('計算機軟體', 'zh-hans')
>>>计算机软体
```