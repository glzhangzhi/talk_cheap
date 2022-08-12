# 简介

就是一个极简的剪贴板IO，能够读取和写入剪贴板的内容

# 安装

`pip install clipboard`

# 读取

```
import clipboard

content = clipboard.paste()
print(content)
```

# 写入

```
import clipboard

content = 'this is not in clipboard'
clipboard.copy(content)
```