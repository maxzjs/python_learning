#/sur/bin/env python3
#求圆面积
#-- codeing:utf-8 --
import os
list1 = ['12.34','9.08','73.1']

def s_sum(r):
	s=3.14*float(r)*float(r)
	print('圆的面积约等于：%d'%s)
for j in list1:
	s_sum(j)
os.system('pause')