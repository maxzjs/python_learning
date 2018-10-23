# 2018-10-23 
# -*- coding -*- 
# 面向对象之枚举类
import os
# 定义常量，用大写变量通过整数来定义
# 更好的方法是为这样的枚举类型定义一个class类型。提供了Enum类实现这个功能

from enum import Enum,unique
Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 这样我们就获得了Month类型的枚举类。可以直接使用Month.Jan来引用一个常量
for name,member in Month.__members__.items():
	print(name,'=>',member,',',member.value)
# value属性则是自动赋给成员int常量，默认从1开始计数
# 可以从Enum派生出自定义类
@unique   # 这个可以检查保证没有重复值   好像直接引用会报错 
# 需要 import unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6
# 访问方法：
print('Weekday.Mon:',Weekday.Mon)
print('Weekday.Sat.value:',Weekday.Sat.value)


os.system('pause')