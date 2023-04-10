# 递归函数：就是内部调用自己
#计算阶乘
import os,time
def fact(n):
	if n = 1:
		return 1
	return n * fact(n-1)
fact(1)
fact(5)
fact(10)
#使用递归需要注意防止栈溢出，递归调用次数过多会导致栈溢出
#解决方法是通过 尾递归优化 /事实上尾递归和循环的效果是一样的
#尾递归是：在函数返回时调用自身本身，并且，return语句不能包含表达式
def fact1(n):
	return fact_iter(n,1)

def fact_iter(num,product):
	if num = 1:
		return 1
	return fact_iter(num-1,num*product)

==>fact_iter(5.1)
==>fact_iter(4,5)
==>fact_iter(3,20)
==>fact_iter(2,60)
==>fact_iter(1,120)
==>120

#大多数编程语言没有针对尾递归做优化，差不多都会溢出
#小结
#递归函数优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出
#可以通过尾递归防止栈溢出。尾递归和循环等价