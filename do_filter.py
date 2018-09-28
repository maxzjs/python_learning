# 2018-9-28 
# -*- coding:utf-8 -*- 
import os
#练习 回数是指从左向右读和从向右和向左读都是一样的数，例如12321,909··· 。请利用filter函数筛选出回数
# n通过切片判断最高位和最低位，第二高位和倒二高位，···是否相同。。先判断长度。之后
'''
def is_palindrome(n):
	for x in range(0,10000):
		while n[x] == n[-(x+1)]:
			return n
'''		
#错误。不对。n不能用切片，不是list或者tuple


#大牛解答：把数字变成字符串（我还没弄清楚python到底有没有字符串的概念没），然后字符串就可以用切片选择了

def is_palindrome(n):
	return str(n) == str(n)[::-1]
output = filter(is_palindrome,range(1,1000))
print(list(output))

os.system('pause')
'''
[::-1] 是list或者tuple倒序。

'''

