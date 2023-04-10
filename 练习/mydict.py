# 2018-11-14 
# -*- coding:utf-8 -*-
# 单元测试
# mydict
import os
class Dict(dict):
	"""docstring for Dict"""
	def __init__(self, **kw):
		super().__init__(**kw)

	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:	
			raise AttributeError(r"'dict' object has no attribute '%s'" %key)
	def __setattr__(self, key, value):
		self[key] = value

d = Dict(a=1,b=2)
print('d["a"]的值:',d['a'])
print('d.a的值:',d.a)


os.system('pause')
