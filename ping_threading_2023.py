# 2018.12.11
# maxzjs
# 批量ping 电脑主机ip
# -*- coding:utf-8 -*-

import threading
import subprocess
import time
import os,sys
from queue import Queue

# 定义工作线程
WORD_THREAD = 50

# 将需要 ping 的 ip 加入队列
IP_QUEUE = Queue()
for i in range(1,255):
    IP_QUEUE.put('10.3.33.'+str(i))

# 定义一个执行 ping 的函数
def ping_ip():
    while not IP_QUEUE.empty():
        ip = IP_QUEUE.get()
        res = subprocess.call('ping -n 2 -w 5 %s' % ip,stdout=subprocess.PIPE)  # linux 系统将 '-n' 替换成 '-c'
        # 打印运行结果
        # 判断ip通不通，通着打印，不通丢弃
        if res != 0:
            pass
        else:
            print(ip,True if res == 0 else False)

if __name__ == '__main__':
    threads = []
    start_time = time.time()
    for i in range(WORD_THREAD):
        thread = threading.Thread(target=ping_ip)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print('程序运行耗时：%s' % (time.time() - start_time))
