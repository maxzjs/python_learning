# 2018-10-6 
# -*- coding:utf-8 -*- 
import os,time
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






os.system("pause")