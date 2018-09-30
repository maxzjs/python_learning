#2018-9-28
import os
# 高级函数之 sorted 排序函数
# sorted 可以对list进行排序
# 可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
sorted([36,5,-12,9,-21])
sorted([36,5,-12,9,-21],key=abs)

#字符串排序，是按照ASCII的大小比较的，通过key函数把字符串映射为忽略大小写排序即可
'''
sorted([36,5,-12,9,-21],key=str.lower) 有问题，会报错
'''
#反向排序，传入第三个参数
'''
sorted([36,5,-12,9,-21],key=str.lower,reverse=True) 会报错
'''
#高阶函数的抽象能力非常强大。
# -*- coding:utf-8 -*- 
#练习 
# 用一组tuple表示学生名字和成绩：

L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]

# 请用sorted对上述列表分别按名字排序
def by_name(t):
	return t[0]
L2 = sorted(L, key=by_name)
print(L2)

# 在按成绩从高到底排序
def by_score(q):
	return q[1]
L2 = sorted(L, key=by_score,reverse=True)   #reverse为真时，反向，默认是从小到大排
print(L2)
os.system('pause')