# 函数参数

# 位置参数
def power(x):
	return x * x
# 位置参数/必选参数
def power2(x,n):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s


# 默认参数 可以传入一个x值，默认n=2/也可以选择传入明确的值，例如 power(5.3)
# 定义默认参数必须指向不变对象
def power3(x,n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s


# 可变参数 传入的参数个数是可变的，可以是0个，也可以是多个;参数自动组装为一个tuple
def calc(numb):
	sum = 0
	for n in numb:
		sum = sum = n * n
	return
#调用时 
calc([1,2,3])
#简化
def calc1(*numb):
	sum = 0
	for n in numb:
		sum = sum + n * n
	return
calc1(1,2,3)
#在参数前加一个*号，参数接收到的是一个tuple，可以传入任意个参数
#有一个list或tuple，调用可变参数
nums = [1,2,3]
calc1(nums[0],nums[1],nums[2])
#简化
calc1(*nums)


# 关键字参数 允许传入任意个 含参数的 参数   关键字参数自动组成为dict
def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)
person('zjs',24)
#可以只传入必选参数


# 命名关键字参数 可以传入任意不熟限制的关键字参数
# 如果！ 要限制关键字参数的名字，用命名关键字参数，例如：只接受city和job作为关键字参数
def person1(name,age,*,city,job):
	pass
#需要特殊分隔符*，*后面的参数视为命名关键字参数
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要特殊分隔符了
def person2(name,age,*args,city,job):
	pass
# 命名关键字参数必须传入参数名，不然会报错
# 命名关键字参数可以有缺省值，简化调用
def person3(name,age,*,city='beijing',job):
	pass
person3('maxjzs',24,job='python')


# 参数组合 5中参数顺序定义：必选参数、默认参数、可变参数、命名关键字参数和关键字参数