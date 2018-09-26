# 2018-9-26 
# /usr/bin/env python3
# -*- coding -*- 
#python 内建的filter函数用于过滤序列
import os
#filter函数把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
#例子：在一个list中，删掉偶数，值保留奇数
def is_odd(n):
	return n % 2 == 1
list(filter(is_odd,[1,2,3,4,5,6,7,8,9,10]))

#把一个序列中的空字符串删掉
def not_empty(s):
	return s and s.strip()

list(filter(not_empty,['A','','B',None,'C',' ']))

#可以用filter求素数
#埃氏筛法，从2开始的所有自然数，构造一个序列
#取序列的第一个数，它一定是素数，然后用2把序列的2的倍数筛掉，依次类推，

def _odd_iter():
	n = 1
	while  True:
		n = n + 2
		yield n
#这是一个生成器，并且是一个无线序列
#然后定义一个筛选函数
def _not_divisible(n):
	return lambda x: x % n > 0

#最后，定义一个生成器，不断返回下一个素数

def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n),it)
	
for n in primes():
	if n < 10000:
		print(n)
	else:
		break







