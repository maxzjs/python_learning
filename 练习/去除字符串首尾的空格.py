#2018-9-18 切片作业
#利用切片操作，实现一个函数，去除字符串首尾的空格
# -*- coding:utf-8 -*-
import os
def trim(s):
	b = 1
	while(b==1):
		if (s[:1]==' '):
				s=s[1:]
		elif (s[-1:]==' '):
				s=s[:-1]
		else:
				b=0
	print(s)
	return s
trim('1hello ')
trim(' 2hello')
trim(' 3heloo ')
trim(' 4hello world ')
trim('5')
trim('   ')
os.system('pause')
#应该还有更优解