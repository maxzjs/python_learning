# 2018-10-19 
# 面向对象高级编程---定制类

import os
# __str__ 返回好看的字符串
# __repr__ 返回程序开发者看到的字符串
# __iter__  可以使一个类用于for...in 循环   用__next__方法拿循环值
class fib(object):
	def __init__(self):
		self.a,self.b = 0,1
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b = self.b,self.a+self.b
		if self.a>100000:
			raise StopIteration()
		return self.a

def fib_yong():
	for aa in fib():
		print(aa)

print(fib_yong())
#print(fib_yong())
# 上面的和list直接取坐标是不行的。需要实现__getitem__ 方法
class fii(object):
	"""docstring for fii"""
	def __getitem__(self,n):
		a,b = 1, 1 
		for x in range(n):
			a,b = b,a+b
		return a 

f = fii()
print('f[0]:',f[0])
print('f[1]:',f[1])
print('f[2]:',f[2])
print('f[100]:',f[100])
# 对于上面的函数做list，切片是不能用的。__getitem__传入的参数可能是int，也可能是一个切片对象slice。要判断
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
F = Fib()
print('F[0:5]:',F[0:5])
# 还需要对很多数值做处理
os.system('pause')