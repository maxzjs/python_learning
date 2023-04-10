# 2018.12.16
# maxzjs
# -*- coding:utf-8 -*-
#  socket_server
import socket, threading, time

# 处理客户端连接
def tcp_link(sock, addr):
    print(('【客户端[%s:%s]已连接】' % addr))
    # 发送连接成功通知
    sock.send('【您已成功连接服务器】'.encode('utf-8'))
    while True:
        try:
            # 接受客户端发送的数据
            data = sock.recv(1024)
            time.sleep(1)
            # 如果接收到空值或者‘exit’则退出
            # not data 表示空值
            if not data or data.decode('utf-8') == 'exit':
                break
            print('Client: %s' % data.decode('utf-8'))
            sock.send(('hello,%s' % data.decode('utf-8')).encode('utf-8'))
        except ConnectionError as e:
            print(e)
            break
    # 断开连接
    sock.close()
    print('【客户端[%s:%s]已断开】' % addr)

# 服务器地址
address = ('127.0.0.1',9999)
# 初始化socket
s = socket.socket()
# 绑定地址
s.bind(address)
# 开始监听
s.listen(5)
print('【服务器已启动，主机：%s, 端口：%s】' % address)
print('【等待连接中···】')
while True:
    # 接收客户端socket和地址
    sock, addr = s.accept()
    # 启动子线程处理连接
    t = threading.Thread(target=tcp_link, args=(sock, addr))
    t.start()



