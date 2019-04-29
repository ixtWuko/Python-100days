"""
Day 14
网络编程
"""
from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread

def tcp_server_test():
    class FileTransferHandler(Thread):
        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient
        def run(self):
            my_dict = {}
            my_dict['filename'] = 'ball.png'
            my_dict['filedata'] = data
            json_str = dumps(my_dict)
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()
    # 创建套接字对象并指定使用哪种传输服务
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('192.168.144.231', 6789))
    server.listen(512)
    print('服务器启动，开始监听...')
    with open('./res/ball.png', 'rb') as f:
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        print('监听到来自 %s 的请求，准备处理' % str(addr))
        FileTransferHandler(client).start()

if __name__ == '__main__':
    tcp_server_test()