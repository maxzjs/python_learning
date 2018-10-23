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
# __getattr__ 
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就回报错。
# 避免错误的话 除了加属性，再有写一个__getattr__方法，动态返回一个属性

class SS(object):
	"""docstring for SS"""
	def __init__(self):
		self.name = 'zjszjs'

	def __getattr__(self,attr):
		if attr == 'score':
			return 99
		# 其他的抛出错误
		raise AttributeError('\'studet\' object has no a attribute \'%s\'' % attr)
sss = SS()
print('sss.name:',sss.name)
print('sss.score:',sss.score)
 # print('sss.age:',sss.age)
# 在没有找到属性的情况下，才调用__getattr__，已有的属性，不会在__getattr__ 中查找
# 要让class只响应特定的几个属性。按约定，抛出Attribute错误

# 可以把一个类的所有属性和方法调用全部动态化处理，不需要任何特殊手段
# 好处就是  可以针对完全动态的情况作调用

# __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。

# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。

class sstu(object):
	"""docstring for sstu"""
	def __init__(self, name):
		self.name = name
	def __call__(self):
		print('Myname is %s.' % self.name)

print(sstu('maxzjsss')())	
# 对象  函数。。有点模糊。。利用 callable函数  可以判断一个对象是否是 可调用 对象
os.system('pause')