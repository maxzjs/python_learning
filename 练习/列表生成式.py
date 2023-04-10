#2018-9-20 
#列表生成式
import os
list(1,11)
L = []
for x in xrange(1,11):
	L.append(x*x)
L

#两层循环 生成排列
[m+n for m in 'ABC' for n in 'XYZ']
#列出当前目录下的所有文件和目录名，python解析器下可以实现
import os
[d for d in os.listdir('.')]

#for循环其实可以同时使用过两个甚至多个变量，比如 dict 的 items() 可以同时迭代key和value
d = {'x':'1','y':'2','z':'3'}
for k,v in d.items():
	print(k,'=',v)

#把一个list中的所有字符串变成小写
l = ['Hello','World','IBM','Apple']
[s.lower() for s in l]

#lower() 不能执行非字符串
#使用内置的  isinstance 函数可以判断一个变量
#作业
L1 = ['Hello','World',18,'Apple',None]
L2 = [a.lower() for a in L1 if isinstance(a,str)]


os.system('pause')