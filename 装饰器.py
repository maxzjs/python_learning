# 2018-10-6 
# -*- coding:utf-8 -*- 
import os,time,functools
'''
函数是对象，函数对象可以被赋值给变量，通过变量也能调用函数
'''
def now():
	print(time.ctime())

f = now
f()
'''
函数对象有一个 __name__ 属性，可以拿到函数名字

'''
print('now.__name__:',now.__name__)
print('f.__name__:',f.__name__)
# 要增强now函数的功能，又不希望修改函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# 本质上，decorator就是一个返回函数的高阶函数。

# 定义一个打印日志的decorator
def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	return wrapper

# 借助python的@语法，把装饰器置于函数的定义处：
@log
def now1():
	print('now1:',time.ctime())
now1()
# 把@log放到now1()函数的定义处，相当于执行了语句： now1 = log(now1)

# 如果decorator 本身需要传入参数，需要写一个返回decorator的高阶函数，更复杂
def log1(text):
    def decorator(func):
        def wrapper1(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper1
    return decorator
@log1('execute')
def now2():
    print('now2：',time.ctime())
now2()
# now2 = log('execute')(now2)
# 上面的函数的__name__ 已经变成wrapper
# 解决方法 内置的functools.wraps 

def log3(func):
    @functools.wraps(func)
    def wrapper3(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper3

def log4(text):
    def decorator1(func):
        @functools.wraps(func)
        def wrapper4(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper4
    return decorator1

#  面向对象（OOP）的设计模式中，decorator称为装饰模式。
#  OOP的装饰模式需要通过继承和组合来实现。
# python可以用函数实现，也可以用类实现装饰器

# 练习 
# 编写一个decorator，能在函数调用前后打印出'begin call'和'end call'的日志
# 再思考一个能否写出一个@log的装饰器 既支持 
'''
@log
def f()
	pass

又支持
@log('execute')
def f()
	pass

'''




os.system("pause")