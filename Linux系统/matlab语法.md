[TOC]

# 简单程序

```matlab
a = 123
x = [1 2 3 4 5]
y1 = [.16 .08 .04]

5 + 5  
3 ^ 2
sin(pi / 2)
7/0
123 * 23.259

%% 一些数学符号的特殊表达式
pi = π，
Inf = ∞
i(和j) = √-1
.Nan = “非数字”
```

# 分号的使用

分号表示结束语句，如果要抑制和影藏表达式的输出，可以在表达式后添加分号

```matlab
x = 3;
y = x + 5
```

# 注释

%用于行注释

还可以使用%{    %}用于块注释

# 常用运算符

|运算符|描述|
|----|----|
|\+ | 相加|
|\-  |相减|
|\*  |标量和矩阵乘法|
|\.* | elementweise阵列乘法 |
|^ | 标量和矩阵求幂|
|\.^ | elementweise阵列求幂 |
|\\ | 左除, a\b == inv(A)*B |
|/  |右除|
|\.\ | elementweise阵列左除？？？ |
|\./ | elementweise阵列右除 |
|:  |生成规则间隔的元素，并表示整个行或列|
|\()  |包含函数参数和数组索引；覆盖优先级|
|\[] | 罩住整列元素|
|\. | 小数点|
|\...  |行连续运算符？？？|
|,  |分隔一行中的语句和元素|
|;  |分隔列并抑制输出显示|
|% | 指定一个注释并指定格式|
|‘  |引用符号和转置运算|
|\.’ | elementweise非共轭转置运算 |
|=  |赋值|

# 关系运算符

|运算符|描述|
|----|----|
|`<` |小于 |
| `<=`| 小于或等于|
|  `>`| 大于|
|  `>=` |大于或等于|
|  `==`| 等于  |
|`~=` |不等于|



# 特殊变量和常数

|常量/变量|描述|
|----|----|
|ans|	最近的运算结果|
|eps	|浮点精度|
|i, j	|  序数单位|
|Inf	| 无穷|
|NaN  |未定义的数值结果|
|pi	  | 圆周率|

# 变量命名规则

字母开头，之后跟任意数量的字母、数字或下划线

大小写敏感

有最大长度限制

# 保存当前变量/加载变量

`save`会保存当前工作空间中的所有变量，在当前目录中以mymat.mat文件保存。

```matlab
save mymat
load mymat
```

# 变量的定义

```matlab
a = 1
b = 2;
c = b + 2
5 + 2
ans
a = 1; b = 2; c = a + b
```

# 显示变量的历史

`who`命令显示使用过的所有变量，`whos`命令将更详细的显示变量的历史，`clear`命令将清除所有变量，如果指定变量名称，则清除指定变量

# 跨行书写

当命令过长时，可以只用...在下一行中继续书写

```matlab
a = bbbbbb + ccccc + ...
	ddddd + e
```

# format格式命令

使用format更改默认的显示格式

```matlab
format long      % 显示十进制小数点后16位
format short     % 默认显示小数点后4位
format bank      % 四舍五入到小数点后2位
format short e   % 用指数方式显示
format long e    % 用指数方式显示
format rat       % 给出最接近结果的合理表达式
format +         %显示正负号
format compact   % 禁止一些换行符
format loose     % 重置为不紧凑的显示模式
```
# 创建向量

向量是一维数组，matlab允许创建两种类型的向量：行向量，列向量

```matlab
r = [1 2 3 4 5]  % 行向量，可以使用逗号或空格分隔元素
c = [1;2;3;4;5]  % 列向量，使用分号来分隔元素
```

# 创建矩阵

矩阵是二维数组，用分号分隔不同行，用逗号或者空格分隔行中的每个元素

```matlab
m = [1 2 3;4 5 6;7 8 9]
```

# 常用命令

## 会话管理

| 命令  | 作用 |
| ---- | ---- |
| clc | 清除命令窗口 |
| clear | 从内存中删除变量 |
| exist | 检查文件或变量是否存在 |
| global | 申明变量为全局变量 |
| help | 搜索帮助信息 |
| lookfor | 搜索帮助信息中的关键字 |
| quit | 停止matlab程序 |
| who | 列出当前变量 |
| whos | 详细列出当前变量 |

## 系统命令
| 命令  | 作用 |
| ---- | ---- |
|cd|进入指定目录|
|date|显示当前日期|
|delete|删除文件|
|diary|打开/关闭日记文件记录|
|dir|列出当前目录下的所有文件|
|load|从文件加载工作区变量|
|path|显示搜索路径|
|pwd|显示当前目录|
|save|将工作区变量保存到文件|
|type|显示文件内容|
|what|列出当前目录中的所有matlab脚本文件|
|wklread|读取.wkl电子表格文件|

## 输入输出命令
| 命令  | 作用 |
| ---- | ---- |
|disp|显示数组或字符串的内容|
|fscanf|从文件读取格式化数据|
|format|控制屏幕显示格式|
|fprintf|对屏幕或文件执行格式化的写入|
|input|显示提示并等待输入|
|；|禁止打印显示|

### `fscanf`和`fprintf`的格式化参数
| 命令  | 作用 |
| ---- | ---- |
|%s|字符串|
|%d|整数|
|%f|浮点数|
|%e|科学计数法|
|%g|最紧凑形式|
|\n|换行|
|\t|制表符|

## 向量，矩阵和数组命令

| 命令  | 作用 |
| ---- | ---- |
|cat|连接数组|
|find|查找非零元素的索引|
|length|计算元素数量|
|linspace|创建规则间隔的向量|
|logspace|创建对数间隔的向量|
|max|返回最大值|
|min|返回最小值|
|prod|产生的每列？？？|
|reshape|改变大小|
|size|计算数组大小|
|sort|对每列进行排序|
|sum|对每列进行求和|
|eye|创建单位矩阵|
|ones|创建一矩阵|
|zeros|创建零矩阵|
|cross|矩阵叉乘|
|dot|矩阵点乘|
|det|计算行列式|
|inv|计算矩阵的逆|
|pinv|计算矩阵的伪逆|
|rank|计算秩|
|rref|计算简化行阶梯形式|
|cell|创建单元格数组|
|celldisp|显示单元格数组|
|cellplot|图形表示单元格数组|
|num2cell|将数组转化为单元格数组|
|deal|匹配输入和输出列表|
|iscell|识别单元格数组|

## 绘图函数

| 命令  | 作用 |
| ---- | ---- |
| axis | 设置轴限制 |
| fplot | 智能绘图 |
| grid | 显示网格线 |
| plot | 生成xy坐标图 |
| print | 保存绘图到文件 |
| title | 在顶部放置文字 |
| xlabel | x轴文本 |
| ylabel | y轴文本 |
| axes | 创建轴对象 |
| close | 关闭当前坐标图 |
| close all | 关闭所有坐标图 |
| figure | 打开一个新图形窗口 |
| gtext | 通过鼠标启用标签方式 |
| hold | 冻结当前坐标图 |
| legend | 通过鼠标放置图例 |
| refresh | 重新绘制当前窗口 |
| set | 指定各种对象的属性 |
| subplot | 在子窗口中创建图 |
| text | 在图中放置字符串 |
| bar | 创建条形图 |
| loglog | 创建日志记录图 |
| polar | 创建极坐标图 |
| semilogx | 创建半标记图（对数横坐标） |
| semilogy | 创建半标记图（对数纵坐标） |
| stairs | 创建梯形图 |
| stem | 创建茎图 |

# 数据类型转换
| 命令  | 作用 |
| ---- | ---- |
|`char` |转换为字符数组(字符串) |
|`int2str` |将整数数据转换为字符串 |
|`mat2str`| 将矩阵转换为字符串 |
|`num2str`| 将数字转换为字符串  |
|`str2double` |将字符串转换为双精度值 |
|`str2num`| 将字符串转换为数字|

# 数据类型确定
| 命令  | 作用 |
| ---- | ---- |
|`is` |检测状态  |
|`isa` |确定输入是否是指定类的对象|
|`iscell` |确定输入是单元格数组  |
|`iscellstr` |确定输入是字符串的单元格数组  |
|`ischar`| 确定项目是否是字符数组|
|`isfield` |确定输入是否是结构数组字段 |
|`isfloat` |确定输入是否为浮点数组|

# 条件判断

```matlab
if a < 20
	fprintf(a)
end
%%%%%%%%%%%%%%%%%%%%%%%%%%
if a < 20
	fprintf(a-1)
else
	fprintf(a+1)
end
%%%%%%%%%%%%%%%%%%%%%%%%%%
if a == 0
	fprintf(0)
elseif( a == 2)
	fprintf(2)
elseif( a == 3)
	fprintf(3)
else
	fprintf(4)
end
%%%%%%%%%%%%%%%%%%%%%%%%%%
if a > 10
	if a == 10
		fprintf('bingo')
	end
end
```

# 选择语句

```matlab
switch(grade)
    case 'A' 
        fprintf('Excellent!\n' );
    case 'B' 
        fprintf('Well done\n' );
    case 'C' 
        fprintf('Well done\n' );
    case 'D'
        fprintf('You passed\n' );
    case 'F' 
        fprintf('Better try again\n' );
    otherwise
        fprintf('Invalid grade\n' );
end
```

# 循环语句

```matlab
while( a < 20)
	fprintf(a)
	a = a + 1
	if a == 11
		break
end
%%%%%%%%%%%%%%%%%%%%%%%%%%
for a = 10:20
	if a == 12
	
	fprintf(a)
end
%%%%%%%%%%%%%%%%%%%%%%%%%%
for a = 1.0:-0.1:0.0
	disp(a)
end
%%%%%%%%%%%%%%%%%%%%%%%%%%
for a = [1 2 3 4 5]
	disp(a)
end
```

