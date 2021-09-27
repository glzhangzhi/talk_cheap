```python
import math
math.sqrt(9)
math.sqrt(8)

import sympy
sympy.sqrt(8)

from sympy import *
x, y = symbols('x y')
expr = x + 2*y
expr
expr + 1
expr - 1
x * expr
expanded_expr = expand(x*expr)
expanded_expr
factor(expanded_expr)

x, t, z, nu = symbols('x t z nu')
init_printing(use_unicode=True)
diff(sin(x) * exp(x), x)  # 求该表达式对于x的导数
integrate(exp(x) * sin(x) + exp(x) * cos(x), x)  # 求该表达式对于x的积分
intrgrate(sin(x ** 2), (x, -oo, oo))  #求该表达式对于x的带上下限的积分
limit(sin(x) / x, x, 0)  # 求x到0的极限
solve(x ** 2 - 2, x) #解这个方程对于x的解

y = Function('y')
dsolve(Eq(y(t).diff(t, t) - y(t), exp(t)), y(t))  # 求ddy - y = e^t的微分方程

Matrix([[1, 2], [2, 2]]).eigenvals()  # 求矩阵特征值

besselj(nu, z).rewrite(jn)  # Rewrite the Bessel function Jν(z) in terms of the spherical Bessel function jν(z)

latex(Integral(cos(x) ** 2, (x, 0, pi)))  # 用公式模式打印带上下限求积分的公式

x = symbols('x')
expr = x + 1
x = 2
expr
expr.subs(x, 2)

x + 1 == 4
Eq(x + 1, 4)

(x + 1) ** 2 == x ** 2 + 2 * x + 1
a = (x + 1) ** 2
b = x ** 2 + 2 * x + 1
simplify(a - b)
c = x ** 2 - 2 * x + 1
simplify(a - c)
a.equals(b)

True ^ False
True ^ True
x ^ y

1 / 2
Rational(1, 2)
```

```python
expr = cos(x) + 1
expr.subs(x, y)  # 用y替代x，也可以用具体的值甚至表达式替代
expr = x ** 3 + 4 * x * y - z
expr.subs([(x, 2), (y, 4), (z, 4)])

expr = x**4 - 4*x**3 + 4*x**2 - 2*x + 3
replacements = [(x**i, y**i) for i in range(5) if i % 2 == 0]
expr.subs(replacements)

str_expr = 'x ** 2 + 3 * x - 1/2'
expr = sympify(str_expr)  # 将字符串转换为运算字符
expr
expr.subs(x, 2)

expr = sqrt(8)
expr.evalf()  # 将结果转换为浮点型
pi.evalf(100)  # 控制浮点精度，默认为15
expr = cos(2 * x)
expr.evalf(subs={x:2.4})
one = cos(1) ** 2 + sin(1) ** 2

import numpy
a = numpy.arange(10)
expr = sin(x)
f = lambdify(x, expr, 'numpy')
f(a)

# 几种不同的打印模式
from sympy import init_printing
init_printing()  # 使用美化打印功能
pprint(Integral(sqrt(1/x), x, use_unicode=False)  # 使用AcsII美化功能， 不传入参数则使用unicode美化功能
```
```python
simplify(sin(x)**2 + con(x)**2)
simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1))
simplify(gamma(x)/gamma(x - 2))

expand((x + 1)**2
expand((x + 2)*(x - 3))

factor(x**2*z + 4*x*y*z + 4*y**2*z)
factor(cos(x)**2 + 2*cos(x)*sin(x) + sin(x)**2)
factor_list(x**2*z + 4*x*y*z + 4*y**2*z)
expand((cos(x) + sin(x))**2)
factor(cos(x)**2 + 2*cos(x)*sin(x) + sin(x)**2)

```
```python
>>> from sympy import *
>>> x, y = symbols('x,y')
>>> y | (x & y)
y | (x & y)
>>> x | y
x | y
>>> ~x
~x

>>> x >> y
Implies(x, y)
>>> x << y
Implies(y, x)

>>> (y & x).subs({x: True, y: True})
True
>>> (x | y).atoms()
{x, y}

And(x ,y)  # x & y
Or(x, y)  # x | y
Not(x)  # ~x
Xor(x, y)  # x 圈加 y
Nand(x, y)  #~(x & y)
Nor(x, y)  # ~(x | y)
Implies(x, y)  # x >> y y << x
Equivalent(x, y) 
to_cnf(~(A | B) | C)  # 转化为合取范式 里或外和
to_dnf(B & (A | C))  # 转化为析取范式 里和外或
is_cnf(A | B | C)  # 判断是否为合取范式
is_dnf(A | B | C)  # 判断是否为析取范式

b = (~x & ~y & ~z) | ( ~x & ~y & z)
simplify_logic(b)  # 将表达式化简成SOP或POS形式
simplify(b)  # 和上一句功能相同

satisfiable(b)  # 求解当xyz为什么时，b表达式为1，没有则返回False
satisfiable(b, all_models=True)  # 并且会返回一个所有满足条件的模型迭代器

def erfuellen(models):
	for model in models:
		if model:
			print(model)
		else:
			print('Die Formel ist unerfuellbar')
erfuellen(satisfiable(mu, all_models=True))

def folgerung(phi, psi):
	return satisfiable(Not(Implies(phi, psi))) == False

def aequivalenz(phi, psi):
	return folgerung(phi, psi) & folgerung(psi, phi)
```