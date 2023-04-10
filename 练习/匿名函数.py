# 2018-10-3 明天可以休息了。
# -*- coding:utf-8 -*- 
import os 
# 匿名函数

print(list(map(lambda x: x * x ,[1,2,3,4,5,6,7,8,9])))

#关键字  lambda 表示 匿名函数 ，冒号前面的x表示函数参数
# 限制为 只能有一个表达式，不用写 return，返回值就是该表达式的结果

# 把匿名函数作为返回值返回
def build(z,y):
	return lambda: z * z + y * y
print(build(4,5)())  # 函数调用   f=build(1,2)  f()   组合

# 练习  改造
def is_odd(n):
	return n % 2 == 1
L = list(filter(is_odd, range(1,20)))

Q = list(filter(lambda x: x % 2 == 1,range(1,20)))
print('改造前',L)

print('改造后',Q)


os.system('pause')