# 2018-10-8 
# -*- coding:utf-8 -*- 
# 偏函数 
# functools 模块提供了很多有用的功能，偏函数（Partial function）
# 个人理解就是 定义新的函数作为基础函数加入额外参数的函数
import os,functools

int('12334') # 把字符串转换为整数，默认按十进制转换
#但是这个函数提供额外的base参数，默认为10。传入的话，可以做N进制的转换
int('12345',base=8)

int('1234556',16)

#假设需要转换大量的二进制字符串，每次传参非常麻烦，可以定义一个函数
# functools.partial 就是帮助我们串讲一个偏函数的，不需要自己定义

int2 = functools.partial(int,base=2)
int2('1000000')
int2('1010110001')

# functools.partial 作用就是把一个函数的某些参数给固定住，返回一个新的函数
# 新函数也可以在调用上传入其他值


# 那个max2 那个没懂



os.system('pause')