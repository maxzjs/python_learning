#2018-9-23 
# -*- coding:utf-8 -*-
#map/reduce 高级函数 
# map() 函数接收两个参数，一个是函数一个是 Iterable，map讲传入的函数依次作用到序列的每个元素，把结果作为新的Iterator返回
from functools import reduce  # reduce 函数使用，要提前引用   python3 内置删掉了reduce
import os
def f(x):
	return x * x

r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))

#reduce 函数是 把一个函数作用在一个序列上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是
# reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)
#求和
def add(l):
	def addre(x1,y1):
		return x1 + y1
	return reduce(addre,l)

print(add([1,2,3,4,5,6]))

# reduce配合map，可以写出把str转换成int的函数
DIGITS = {'0':0,'1':1,'2':2,'3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return DIGITS[s]
	return reduce(fn,map(char2num,s))
print(str2int('21324145'))

#lambda 函数，又称匿名函数 简化函数，不用命名
'''
对比上面
def str2int(s):
	return reduce(lamdba x,y:x*10+y,mapr(charnum,s))
'''


#练习1：
#利用map函数，把用户输入的不规范的英文名字，变成首字母大写，其他小写的规范名字
#输入：['adam','LISA','barT']
def normalize(name):
	return name[0].upper() + ''.join(name.lower()[1:])

#测试：
L1 = ['adam','LISA','barT']
L2 = list(map(normalize,L1))
print(L2)

#用了 upper 和 lower 函数




#练习2：
#编写一个prod函数，可以接受一个list并利用reduce求积
def prod(L):
	def q(x,y):
		return x*y
	return reduce(q,L)
#简化
'''
def prod1(L1):
	return reduce(lamdba x,y:x*y,L1)
'''
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


#练习3：
#利用map和reduce编写一个str2float函数，把字符串'123.456'变成浮点数123.456：
#解读：找到处理小数点的方法（难点）。
def str2float(s):
    w=s.index('.')
    return reduce(lambda x,y:x*10+y,map(char2num, s[:w]+s[w+1:]))/pow(10, len(s)-1-w)	
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
#练习3暂时失败


os.system('pause')