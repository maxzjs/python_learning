# 2018-9-30 明天国庆了
# -*- coding:utf-8 -*- 
import os
# 函数返回值 除了可以接收函数作为参数外，还可以把函数作为结果值返回

# 实现一个可变参数的求和

def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n 
	return ax

# 如果不需要立刻求和 ，而是在后面的代码中，根据需要再计算，返回求和的函数

def lazy_sum(*args):
		def sum():
			axa = 0
			for na in args:
				axa = axa + na
			return axa
		return sum

f = lazy_sum(1,3,5,7,9)
print(f())					
'''
在函数lazy_sum中又定义函数sum，内部函数sum可以引用外部函数的参数和局部变量，外函数返回函数sum，相关参数和变量都保存在返回的函数中，这就是闭包

！！ 调用闭包函数时，每次调用都会返回一个新的函数

返回函数不要引用任何循坏变量，
'''
f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
print(f1==f2)
'''
'''
def count():
	fs = []
	for i in range(1,4):
		def ff():
			return i * i
		fs.append(ff)
	return fs
f11,f22,f33 = count()
print(f11(),f22(),f33())
'''
返回的函数引用了变量i，等到3个函数都返回时，他们所引用的变量i已经变成了3


一定要引用循环变量咋整？ 再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定掉函数参数的值不变
'''
def count1():
	def fff(j):
		def g():
			return j * j
		return g
	fss = []
	for x in range(1,4):
		fss.append(fff(x))
	return fss
g1,g2,g3 = count1()
print(g1(),g2(),g3())
'''
练习
利用闭包返回一个计数器函数，每次调用它返回递增整数
'''
'''
def createCounter():
	def counter(q):
		def cc():
			return  q + 1
		return cc
	ccf = []
	for nn in range(1,100):
		ccf.append(counter(nn))
	return ccf
'''
#counterA = createCounter()

# 有问题，返回值不对
# 写于2018-10-3 
'''

'''
def createCounter():
	L = [0]
	def counter():
		L[0] += 1
		return L[0]
	return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
'''
闭包中内部函数要修改外部函数局部变量L，只有两个办法：
1.把局部变量变成一个容器（变成可变对象），然后就OJBK了

2.在内部函数里给外部变量加一个 nonlocal 声明，指示内部函数去其他领域获取这个变量
'''
os.system('pause')