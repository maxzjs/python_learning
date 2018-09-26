#!/usr/bin/python
# -*- coding:utf-8 -*-
import time,os

number=input('小伙子你压死我几只鸡？')
number=int(number)
years=0
chicken=number
smallchicken=0
while years < 10:
        chicken=chicken+smallchicken
        smallchicken=chicken*100
        years+=1
chicken=chicken+smallchicken
time.sleep(1)
print('小伙子，我们都是老实本分的人')
time.sleep(1)
print('这都是散养的生态鸡，养的老慢了')
time.sleep(1)
print('我们平常都得养1年才能养大呢，都有感情了')
time.sleep(1)
print('也不敢骗你，一只鸡一年下100个蛋不过分吧')
time.sleep(1)
print('小伙子，你算算，这要是10年下来，你这不得陪我们%d只鸡啊'%chicken)
time.sleep(1)
print('你现在还觉得500一只鸡贵吗？')

os.system('pause')