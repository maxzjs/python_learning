# 2018-10-14
# 面向对象编程--访问限制
# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。
# 在python（差不多的编程语言中），把变量写成私有变量，只有内部可以访问，外部不能访问。
import os

class students(object):

	def __init__(self,name,score):
		self.__name = name
		self.__score = score
# 这样已经从外部无法访问实例变量了
# 这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。

# 如果外部代码想要获取name和score，可以增加方法：

	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score

	def set_name(self,name):
		self.__name = name
	def set_score(self,score):
		self.__score = score
# 又要允许代码修改score，增加方法：
# 在方法中对参数做检查，避免传入无效或者错误的参数
	def set_score1(self,score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')
		

	def print_score(self):
		print('%s,%s' % (self.__name,self.__score))

# 练习 
# 把student对象的gender字段对外隐藏起来，用方法代替
class Stu(object):
	"""docstring for Stu"""
	def __init__(self, name,gender):
		self.__name = name
		self.__gender = gender
	def get_gender(self):
		return self.__gender
	def set_gender(self,gender):
		self.__gender = gender	

bart = Stu('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
# 解决ok
# 和C#的构建私有变量方法道理一样。。只是把 get和set分开写到两个def中
os.system('pause')