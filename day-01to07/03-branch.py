"""
Day 3
分支

Author: ixtwuko
"""

import getpass
import math

def authenticate():
    username = input('请输入用户名：')
    password = getpass.getpass('请输入密码：')
    if username == 'admin' and password == '123456':
        print('身份验证成功！')
    else:
        print('身份验证失败！')

def unit_conversion():
    value = float(input('请输入长度：'))
    unit = input('请输入单位：')
    if unit == 'in' or unit == '英寸':
        print('%f英寸 = %f厘米' % (value, vlaue * 2.54))
    elif unit == 'cm' or unit == '厘米':
        print('%f厘米 = %f英寸' % (value, value / 2.54))
    else:
        print('请输入有效单位！')

def triangle():
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    if a + b > c and a + c > b and b + c > a:
        print('周长：%f' % (a + b + c))
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print('面积：%f' % area)
    else:
        print('这不是一个三角形！')

if __name__ == '__main__':
    authenticate()
    unit_conversion()
    triangle()