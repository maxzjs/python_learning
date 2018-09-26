# 2018-9-23 
# 高级函数 
#就是让函数的参数能够接收的函数
#函数式变成就是指这种高度抽象的编程范式
# -*- coding:utf-8 -*-
import os
def add(x,y,f):
	return f(x) + f(y)

print(add(-5,6,abs))

os.system('pause')
	