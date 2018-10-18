# 2018-10-18
# 面向对象之实例属性和类属性
# 
import os
# 由于Python是动态语言，根据类创建的实例可以任意绑定属性。

# 给实例绑定属性的方法是通过实例变量，或者通过self变量：
class Student(object):
    def __init__(self, name):
        self.name = name

#print('s.score:',s.score)
# 但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有:

class students(object):
	name = 'students'
ss = students() # 创建实例ss
print('ss.name: ',ss.name)
print('students.name: ',students.name)
ss.name = 'zjs'
print('ss.name: ',ss.name)

print('students.name: ',students.name)

del ss.name

print('ss.name: ',ss.name)
# 练习 :为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加

class stu(object):
	count = 0
	"""docstring for stu"""
	def __init__(self, name):
		self.name = name
		stu.count += 1   # 真笨，这么简单的都没想到
# 测试:
if stu.count != 0:
    print('测试失败!')
else:
    bart = stu('Bart')
    if stu.count != 1:
        print('测试失败!')
    else:
        lisa = stu('Bart')
        if stu.count != 2:
            print('测试失败!')
        else:
            print('Students:', stu.count)
            print('测试通过!')


os.system('pause')