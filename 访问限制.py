# 2018-10-14
# 面向对象编程--访问限制
# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。
# 在python（差不多的编程语言中），把变量写成私有变量，只有内部可以访问，外部不能访问。
import os

class students(object):

	def __init__(self,name,score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print('%s,%s' % (self.__name,self.__score))
# 这样已经从外部无法访问实例变量了
# 这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。




os.system('pause')