# 2018.12.29
# maxzjs
# -*- coding:utf-8 -*-

import random

def ran_sum_hong():
    a = random.randint(1,33)
    return a

def ran_sum_lan():
    b = random.randint(1,16)
    return b

def ssq():
    list = []


    for x in range(10):
        if len(list) < 6:
            val_h = ran_sum_hong()
            if val_h not in list:
                list.append(val_h)
        else:
            pass
    list.sort(reverse=False)
    val_l = ran_sum_lan()
    list.append(val_l)

    print("本次随机的双色球彩票号码为：",list,"前6位红色球，最后一位蓝球")


ssq()