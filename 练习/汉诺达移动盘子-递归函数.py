#sur/bin/env python3
#利用递归函数移动汉诺塔
#它接收参数你，表示3个珠子A,B,C中第一个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
# -*- coding:utf-8 -*-
import os
def move(n,a,b,c):
	if n == 1:
		print('move',a,'-->',c)
	else:
		move(n-1,a,c,b)   # a的 n-1 放b
		move(1,a,b,c)     # 最后一个放c
		move(n-1,b,a,c)   # b的放c

move(3,'A','B','C')
os.system('pause')
#没懂？  

## 评论解析
# 在递归的思想里，把问题简单化。
# n个盘子，从a经过b移动到c，分三步
# 1.把最上面的（n-1）个盘子从a，经过c移动到b
# 2.把1个盘子，从a直接移动到c
# 3.把b上的n-1个盘子从b经过c    至于怎么把n-1个盘子移过去，那是另一层move干的事，我不管。