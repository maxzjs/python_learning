# 2018.12.5
# maxzjs
# -*- coding:utf-8 -*-
# 常用内建模块 itertools

import itertools
from functools import reduce
natuals = itertools.count(1)
'''
for n in natulas:
    print(n)
    
count()会创建一个无线的迭代器，for循环会打印出自然数序列，
cycle()会把传入的一个序列无限重复下去

repeat() 负责把一个元素无限重复下去，可以提供第二个参数，限定重复次数
'''
ns = itertools.repeat('A',10)
for nn in ns:
    print(nn)
print('```````')
# 无限序列只有在for循环才会无限迭代下去，如果只是创建了一个迭代对象，他不会事先吧无限个元素生成出来。
# 通常我们会通过takewhile()等函数根据条件判断截取出一个有限的序列

nss = itertools.takewhile(lambda x: x <= 10,natuals)
print(list(nss))
print('```````')
'''
chain()可以把一组迭代对象串联起来，形成一个更大的迭代器

'''
for c in itertools.chain('abc','xyz'):
    print(c)

print('```````')
'''
groupby() 把相邻的重复元素跳出来放在一起
'''
for key, group in itertools.groupby('aaabbbccaaa'):
    print(key,list(group))

print('```````')

# 练习：计算圆周率可以根据公式：利用itertools模块，计算这个序列的前N项和：

def pi(N):
    '计算pi的值'
    # step 1: 创建一个奇数序列：1,3,5,7,9,...
    odd = itertools.count(1,2)
    # count(x,y)  x从几开始，y代表间隔的位数，count(1,2)代表从1开始，取奇数
    # step 2: 取该序列的前N项：1,3,5,7,9, ... , 2*N-1.
    aa = itertools.takewhile(lambda b: b <= 2*N-1, odd)
    # step 3: 添加正负符号并用4除：4/1,-4/3,4/5,-4/7,4/9,...
    c = itertools.cycle([1,-1])
    aa = map(lambda x: (4 / x) * next(c), aa)
    # step 4:求和：
    sums = reduce(lambda x,y: x+y, aa)
    return sums

# 测试:
print("测试：")
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')



