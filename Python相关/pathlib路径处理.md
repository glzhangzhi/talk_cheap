[TOC]

```python
from pathlib import Path
path = Path()
```

# 当前目录和主目录

```
path.cwd()
path.home()
```

# 创建新目录

```
new_path = path / "new"
newpath.mkdir()
```

# 连接路径

```
new_path = path / 'Document'
new_path = path.joinpath('Document')
```

# 创建空文件

```
path('newfile.txt').touch()
```

# 重命名

```
file = path('somefile.txt')
path.rename('new_name.txt')
```

# 路径拆分

```
path = Path('C:/Users/A/B')
path.parts
```

# 文件名拆分

```
path = Path('C:/Users/A/B/file.txt')

path.name  # 文件名
path.stem  # 前缀
path.suffix  # 后缀
```

# 目录内容名字遍历

```
path = Path('C:/Users/A/B')

for dir in path.iterdir():
	if dir.is_dir():
		print('dir')
	if dir.is_file():
		print('file')
```

# 目录内容遍历筛选

```
path = Path('C:/Users/A/B')

for dir in path.glob("*.py"):
	if dir.is_dir():
		print('dir')
	if dir.is_file():
		print('file')
```

# 读取文本文件

```
path = Path('word.txt')
content = path.read_text()
```

# 打开文件

```
path = Path('word.txt')

with path.open() as f:
	lines = f.readlines()
	print(lines)
	
for line in lines:
	print(line.rstrip())
```

# 写入文件

```
path = Path('myfile.txt')
path.touch()
path.write_text('This is myfile.txt')
```

# is条件判断

```
path.exists()  # 是否存在
path.is_dir()  # 是否是目录
path.is_file()  # s
```



