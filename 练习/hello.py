# 2018-10-10 
# -*- coding:utf-8 -*-
#!/usr/bin/env python3
'a test module'   # 文档注释

__author__ = 'maxzjs'
import sys

def test():
	args = sys.argv
	if len(args)==1:
		print('world,hello!')
	elif len(args)==2:
		print('hello,%s!' %args[1])
	else:
		print('Too many arguments!')

if __name__ == '__main__':
	test()

'''
当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
'''
'''
作用域
私有变量和函数，通过加 _ 单下划线来标识
__xxx__ 是特殊变量，可以直接被引用

实现代码封装和抽象方法

'''

