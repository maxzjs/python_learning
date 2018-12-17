'''
廖雪峰UDP编程讨论的简易聊天室，拔下来的
需要读代码，理清代码思路。学习学习
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/12/6 14:10
# @Author : Mr.Zuo
# @File : chatrom.py
# @desc : 简易聊天室
import socket
import threading
import logging

# 客户端 数据分隔符
CLIENT_SPLIT = ']]][[['
# 消息编码
MESSAGE_ENCODING = 'utf-8'
# TCP最大等待连接数
TCP_MAX_WAITING = 10
# 一次读取字节数
BUFFER_SIZE = 1024
# 默认主机名和端口
DEFAULT_ADDRESS = ('127.0.0.1', 8080)
logging.basicConfig(level=logging.INFO)


# 聊天室服务器
class Server(socket.socket):

    def __init__(self, address=DEFAULT_ADDRESS):
        super(Server, self).__init__(type=socket.SOCK_DGRAM)
        # 服务器地址
        self.__address = address
        # 保存客户端信息 key为用户名 value为用户地址
        self.__clients = dict()

    # 启动服务器
    def start(self):
        # 绑定UDP地址
        self.bind(self.__address)
        logging.info('【服务器已启动，主机：%s，端口：%s】' % self.__address)
        while True:
            try:
                # 接收用户消息
                data, addr = self.recvfrom(BUFFER_SIZE)
                data = data.decode(MESSAGE_ENCODING)
                # 如果data不包含分隔符，则是第一次发送
                if CLIENT_SPLIT not in data:
                    # 将该用户存入客户端字典
                    self.__clients[data] = addr
                    self.sys_message('欢迎%s进入聊天室' % data)
                else:
                    # 向聊天室广播
                    self.user_message(data, addr)
            except ConnectionError as e:
                logging.debug(e)

    # 像聊天室所有用户发送信息(除发送消息的用户)
    def user_message(self, msg, from_address=None):
        logging.info('接收到消息：%s' % msg)
        logging.info('当前客户端：%s' % self.__clients)
        for name, address in self.__clients.items():
            # 排除发送消息的客户端
            if from_address != address:
                self.sendto(msg.encode(MESSAGE_ENCODING), address)

    # 发送系统消息
    def sys_message(self, msg):
        msg = 'sys' + CLIENT_SPLIT + msg
        for name, address in self.__clients.items():
            self.sendto(msg.encode(MESSAGE_ENCODING), address)


# 聊天室客户端
class Client(socket.socket):

    def __init__(self, name, address=DEFAULT_ADDRESS):
        super(Client, self).__init__(type=socket.SOCK_DGRAM)
        # 服务器地址
        self.__address = address
        # 聊天室昵称
        self.__name = name

    # 启动客户端
    def start(self):
        logging.info('【客户端已启动】')
        # 启动后向服务器发送昵称和客户端地址
        self.sendto(self.__name.encode(MESSAGE_ENCODING), self.__address)
        # 启动子线程接收服务器消息
        t = threading.Thread(target=self.recv_handler)
        t.start()
        while True:
            msg = input()
            self.send_msg(msg)

    # 发送消息
    def send_msg(self, msg):
        # 将用户昵称加入消息
        data = (self.__name+CLIENT_SPLIT+msg).encode(MESSAGE_ENCODING)
        # 发送消息至服务器
        self.sendto(data, self.__address)
        self.show_msg(data)

    # 打印消息
    def show_msg(self, data):
        name, msg = data.decode(MESSAGE_ENCODING).split(CLIENT_SPLIT)
        if name == 'sys':
            print('----------%s----------' % msg)
        elif name == self.__name:
            print('%s：%s' % (name, msg))
        else:
            print('\t\t\t\t\t\t%s：%s' % (msg, name))

    # 接收服务器发送的数据
    def recv_handler(self):
        while True:
            data = self.recv(BUFFER_SIZE)
            self.show_msg(data)



# 创建服务器
from chatrom import Server

server = Server(address=('127.0.0.1', 8080))

server.start()

# 创建客户端
from chatrom import Server
c = Client('Alex1', address=('127.0.0.1', 8080))

c.start()

