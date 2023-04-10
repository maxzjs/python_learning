# 2018-9-19 
#给定一个list或者tuple，通过for循环遍历这个list或者tuple，称为迭代
#python的for循环抽象成都高于C的。
#默认下，dict迭代的是key。要迭代value，可以用 for value in d.values()
#要痛死迭代key和value，用 for k,v in d.items()
#如何判断一个对象是可迭代对象。通过  collections模块的 Ilerable类型判断

#内置的 enumerate 函数可以吧一个list变成索引-元素对，
import os
for i,value in enumerate(['A','B','C']):
	print(i,value)
os.system('pause')
