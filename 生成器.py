#2018-9-18 -*- coding:utf-8 -*- 
#生成器 可以一边循环一边计算生成大数据列表，防止占用过多内存
#生成器：generator

import os
#普通列表
L = [x*x for x in range(10)]
#生成器
g = (x*x for x in range(10))
#一个一个打印的话通过 next() 函数获得下一个返回值
#generator保存的是算法，每次next就计算出下一个元素的值。直到最后一个元素
#正确的方法是用for循环
for n in g:
	print(n)


os.system('pause')