#-*- coding: utf-8 -*- 
#2018-9-20 
# 斐波拉契数列（Fibonacci） 除了第一个和第二个数外，任意一个数都可以由前两个数相加得到
#1,1,2,3,5,813,21,34，····
import os
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		print(b)
		a,b = b,a+b
		n = n + 1
	return 'done'
fib(10)
#定义生成器	
def fib1(max1):
	n1,a1,b1 = 0,0,1
	while n1 < max1:
		yield b1
		a1,b1 = b1, a1+b1
		n1 = n1 + 1
	return 'done1'	
#fib(10)
#把print换成yield 关键字，就变成一个generator 
#生成器和函数的执行流程不一样。函数是顺序执行，遇到return语句就返回。
#生成器在每次调用next的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句出执行

#例子 定义一个生成器，一次返回数字1,3,5
def odd():
	print('step1')
	yield 1
	print('step2')
	yield(3)
	print('step3')
	yield(5)
o = odd()   #调用generator时，首先生成一个generator对象，
next(o)
next(o)
next(o)

#用for循环调用生成器时，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib1(6)
while True:
	try:
		x = next(g)
		print('g',x)
	except StopIteration as e:
		print('Generator retuan value:',e.value)
		break


os.system('pause')