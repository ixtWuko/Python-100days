"""
Day 14
网络编程
"""

from socket import socket
from json import loads
from base64 import b64decode

def tcp_client_test():
    client = socket()
    client.connect(('192.168.144.231', 6789))
    in_data = bytes()
    data = client.recv(1024)
    while data:
        in_data += data
        data = client.recv(1024)
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open('./res/receive-'+filename, 'wb') as f:
        f.write(b64decode(filedata))
    print('图片已保存！')

if __name__ == '__main__':
    tcp_client_test()