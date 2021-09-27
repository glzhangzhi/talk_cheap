def gcd(a, b):
	'''求最大公约数

	'''
	a, b = (a, b) if a >= b else (b, a)
	while b:
		a, b = b, a % b
	return a

def lcm(a, b):
	'''求最小公倍数

	'''
	return a * b // gcd(a, b)


def phi(n:str) -> int:
	'''求欧拉函数值

	参数：
		n：要求的数

	返回值：
		n的欧兰函数值

	'''
	res = n
	for i in range(2,n+1):
		if n % i == 0:
			n /= i
			res = res - res / i
		while n % i == 0:
			n /= i
	return res


def pri(x):
	'''判断一个数是不是质数


	'''
	for i in range(2, x - 1):
		if (x % i == 0):
			return True
		else:
			continue
	return False

def fen(x):
	for i in range(2, int(x - 1)):
		if (x % i == 0):
			if (pri(i) == 1):
				return i, x / i
	return 1, x

def fenjie(k):
	'''
	将输入数字作因数分解,得到质因数和剩余值

	'''
	print(k,'=')
	cheng, yu = fen(k)
	while (cheng != 1):
		print (cheng, '*')
		cheng, yu = fen(yu)
	print(yu)

def oula(A, C):
	'''
	欧拉算法

	'''
	ap = A
	cp = C

	while 1:
		c = ap
		a = cp%ap
		b = cp//ap
		print('%d = %d - %d * %d' % (a, cp, ap, b))
		if a == 1:
			break
		ap = a
		cp = c

def binar(x):
    '''
    转换二进制

    '''
    A = int(x // 1)
    if x % 1 != 0:
        B = x % 1
    else:
        B = None
    ausgabe1 = ''
    while A != 0:
        a = A // 2
        b = A % 2
        ausgabe1 = str(b) + ausgabe1
        A = a
    if ausgabe1 == '':
        ausgabe1 = '0'
    if B != None:
        ausgabe2 = ''
        xx = str(B).split('.')[-1]
        while xx != '0':
            ausgabe2 += str(int((B * 2) // 1))
            B = (B * 2) % 1
            xx = str(B).split('.')[-1]
        return ausgabe1 + '.' + ausgabe2
    else:
        return ausgabe1

def IEEE754(n):
    '''
    计算浮点数的IEEE754结果，需要依赖二进制转换函数

    '''
    if n >= 0:
        a = 0
    else:
        a = 1
        n = n * -1
    bn = float(binar(n))
    if str(bn)[0] == '0':
        X = str(bn).split('.')[-1]
        count = 0
        for x in X:
            count += 1
            if x != '0':
                break
        bn = str(bn).replace('.', '')
        print(bn)
        print(count)
        c = bn[count] + '.' + bn[count + 1:]
        b = count * -1
    else:
        print(bn)
        b = len(str(bn).split('.')[0]) - 1
        bn = int(str(bn).replace('.', ''))
        print(bn)
        c = str(bn)[1:]
        print(c)
    result = str(a) + str(binar(b + 127)) + c.split('.')[-1]
    rest = 32 - len(result)
    restr = '0' * rest
    result += restr
    return result


print(gcd(144, 274))