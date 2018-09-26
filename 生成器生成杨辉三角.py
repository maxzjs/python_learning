#2018-9-21
#练习 用generator生成器 生成 杨辉三角
# -*- coding:utf-8 -*- 

import os
def triangles():
    row = [1]
    while True:
        yield(row)
        row = [1] + [row[k] + row[k + 1] for k in range(len(row) - 1)] + [1]

# 不是特别明白，慢慢来可以缕清思路
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
os.system('pause')