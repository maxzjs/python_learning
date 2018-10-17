# 2018-10-16 
# -*- coding:utf-8 -*- 
# 面向对象编程--继承和多态
import os
'''
当定义class时，可以从现有的class继承，新的class称为子类，被继承的是基类、父类或超类
'''
class Animal(object):
	"""docstring for Animal"""
	def run(self):
		print('Animal is running...')
# 编写Dog和Cat类时，可以直接从Animal类继承

class Dog(Animal):
	pass


class Cat(Animal):
	pass
# 继承获得父类的全部功能。自动拥有run方法
dog = Dog()
print('dog.run():')
dog.run()
cat = Cat()
print('cat.run():')
cat.run()
# 可以对子类增加一些方法
class Dog1(Animal):
	def run(self):
		print('Dog is running')
	def eat(self):
		print('Eating meat')
# 可以对子类改进

class Cat1(Animal):
	def run(self):
		print('Cat is running')
# 子类的方法会覆盖基类的同名方法
# 数据类型，子类继承于基类
b = Animal()
print('isinstance(b,Dog):',isinstance(b,Dog))

def run_twice(animal):
	animal.run()
	animal.run()
print('run_twice(Animal()):',run_twice(Animal()))
print('run_twice(Dog1()):',run_twice(Dog1()))
print('run_twice(Cat1()):',run_twice(Cat1()))


# 不同子类继承于基类，然后不同子类可以修改方法，且正常运行，原因在于多态
# 静态语言需要传入数据类型，传入的对象必须是基类类型或者它的子类。
# python是动态语言，不一定需要传入基类类型。只需要保证传入的对象有一个run方法就OK


os.system('pause')