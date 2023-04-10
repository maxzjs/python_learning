# 十进制转二进制
#dec = input('输入十进制数：')
import os,time
def Dec2Bin(dec):
	result = ''

	if dec:
		result = Dec2Bin(dec // 2)
		return result + str(dec % 2)
	else:
		return result

print(Dec2Bin(32))
os.system("pause")