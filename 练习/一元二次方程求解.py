#定义函数，接受3个参数，返回一元二次方程的解
#/usr/bin/env python3
import os,math
def quadratic(a,b,c):
	n = (b*b)-(4*a*c)
	if n < 0:
		print('该方程无有理数解')
		return 0
	else:
		x1 = (-b + math.sqrt(n)) / (2*a)
		x2 = (-b - math.sqrt(n)) / (2*a)
		print(x1,x2)
		return 0
a = float(input('请输入a的值：'))
b = float(input('请输入b的值：'))
c = float(input('请输入c的值：'))
quadratic(a,b,c)
os.system('pause')



