直接上语法规则

python中自带了re库，以支持正则表达式的使用
```python
import re
```
常用方法

```python
pattern = re.compile(string[,flag]) #通过在参数中传入原生字符串对象，生成pattern队形，利用这个对象进行进一步的匹配
re.match(pattern, string[, flags]) #从string的第一个字符开始匹配，如果有相符合的，就返回T，如果遇见只符合pattern前几个字符的，返回F，到字符串结尾仍未匹配到，也返回F
```

match返回的对象有如下属性和方法：（只介绍了部分）
string 匹配使用的字符串
re 匹配使用的pattern对象
pos 开始搜索的索引
endpos 结束搜索的索引

```python
re.search(pattern, string[, flags]) #过程与match类似，不同的是search方法不从字符串第一个字符开始匹配
re.splite(pattern, string[, maxsplit]) #使用pattern将string分割，maxsplit指定最大分割次数，不指定将全部分割
re.findall(pattern, string[, flags]) #以列表形式返回全部能匹配的子串
re.finditer(pattern, string[, flags]) #以顺序访问迭代器的形式返回全部能匹配的子串，可以使用for循环读取
re.sub(pattern, repl, string[, count]) #使用repl替换string中每一个匹配的子串后返回替换后的字符串，count指定最多替换次数
re.subn(pattern, repl, string[, count]) #返回 (sub(repl, string[, count]), 替换次数)
```

flags参数的可选值有：
re.I 忽略大小写
re.M 多行模式，改变^和$的行为模式
re.S 点任意匹配模式
re.L 使预定字符类\w \W \b \B \s \S 取决于当前区域设定
re.U 使预定字符类\w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
re.X 详细模式，这个模式下正则表达式可以是多行的，忽略空白字符，并可以加入注释
如果在生成pattern的时候已经注明了flag参数，则不需要在使用pattern的时候再次注明