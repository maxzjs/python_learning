# 2018-10-17
# -*- coding:utf-8 -*- 
# 面向对象编程之获取对象信息
import os
# 获取对象信息  
# type() 判断对象类型

print('123:',type(123))
print('str:',type('str'))

# 一个变量指向函数或者类，也可以用type判断
# type返回是对应的class类型
# 对于类的继承关系，可以使用isinstance函数
print('isinstance([1,2,3]):',isinstance([1,2,3],(list,tuple)))
# 使用dir函数，可以获得一个对象的所有属性和方法，返回一个包含字符串的list

print('dir(ABC):',dir('ABC'))

# 类似__XXX__ 的属性和方法都是特殊用途。__len__方法返回长度

print('len(ABC):',len('ABC'))
print('len(ABC):','ABC'.__len__())
'''
 配合
 getattr()---获取xxxx属性   
 setattr()---设置xxxx属性   
 hasattr()---是否有xxxx属性    
 可以操作一个对象的状态
'''

os.system('pause')