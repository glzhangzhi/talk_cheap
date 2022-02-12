# 安装

```
pip install -U arrow
import arrow as aw
```

# 获取现在的时间

```
aw.now()
aw.utcnow()
aw.now('US/Pacific')
```

# 从时间戳创建时间

```
aw.get(1367900664)
aw.get(1367900664.152325)
```

# 从字符串创建时间

```
aw.get('2013-05-05 12:30:45', 'YYYY-MM-DD HH:mm:ss')
```

# 获取时间中的各个单位量

```
a = aw.now()
a.year
a.date()
a.time()
```

# 替换/推算时间中的各个量

```
a = aw.now()
a.replace(hour=10, minute=40)
a.shift(days=+3)
a.shift(hours=-2)
```

# 格式化时间表示

```
a.format('YYYY-MM-DD HH:mm:ss')
```

