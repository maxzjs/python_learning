# 2018.12.11
# 更新时间：2023.4.10
# 作者：maxzjs
# 批量ping 电脑主机ip
# -*- coding:utf-8 -*-

import threading
import subprocess
import time
import ipaddress
import os, sys
from queue import Queue



# 定义工作线程
WORD_THREAD = 10

# 将需要 ping 的 ip 加入队列
IP_QUEUE = Queue()



# 判断ip地址是否正确
def judge_ip(ip):
    ip_str = ip
    ip_list = ip_str.split(".")  # 将字符串按点分割成列表
    for num in ip_list:
        if len(ip_list) == 4 and num.isdigit() and 0 <= int(num) <= 255:
            continue
        else:
            ip = input("请输入ip地址：")
            return judge_ip(ip)



i_ip = input("请输入ip地址：")
i_mask = input("请输入子网掩码：")
jud = judge_ip(i_ip)
i_ip_add = i_ip + '/' + i_mask
ip_net_add = ipaddress.ip_interface(i_ip_add).network
ipadd_net = ipaddress.ip_network(str(ip_net_add))
for n in ipadd_net.hosts():
    IP_QUEUE.put(str(n))

# 定义一个执行 ping 的函数
def ping_ip():
    while not IP_QUEUE.empty():
        ip = IP_QUEUE.get()
        res = subprocess.call('ping -n 2 -w 5 %s' % ip, stdout=subprocess.PIPE)  # linux 系统将 '-n' 替换成 '-c'
        # 打印运行结果
        # 判断ip通不通，通着打印，不通丢弃
        Note = open('ping_True.txt', mode='a')
        if res != 0:
            pass
        else:
            print(ip, True if res == 0 else False)
            Note.write(ip)
            Note.write('\n')
        Note.close()


if __name__ == '__main__':
    print("批量ping多个IP地址(网段)")
    threads = []
    start_time = time.time()
    for i in range(WORD_THREAD):
        thread = threading.Thread(target=ping_ip)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print('程序运行耗时：%s' % (time.time() - start_time))


