安装

```shell
pip install py2exe
```

编译脚本

假设要打包的文件为myprogram.py，首先新建一个名为 setup.py 的脚本文件，内容如下

```python
from distutils.core import setup
import py2exe

setup(console=['myprogram.py'])
```

之后在命令行执行

```
python setup.py py2exe
```

会在当前文件夹生成一个dist文件夹，里面就是所有执行脚本需要的文件，运行其中的myprogram.exe就行。

注意复制给其他人的时候，需要把整个文件夹里的文件都复制进去。