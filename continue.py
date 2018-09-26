# continue 跳过循环 打印奇数
import os,time
n = 0
while n < 10:
	n = n + 1
	if n % 2 == 0:
		continue
	print(n)
os.system('pause')