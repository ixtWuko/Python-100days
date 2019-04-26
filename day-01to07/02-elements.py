"""
Day 2
语言元素

Author: ixtWuko
"""

import math

def Fahrenheit_to_Celsius():
    f = float(input("请输入华氏温度："))
    c = (f - 32) / 1.8
    print('%.1f华氏度 = %.1f摄氏度' % (f, c))

def cycle():
    radius = float(input('请输入圆的半径：'))
    perimeter = 2 * math.pi * radius
    area = math.pi * radius * radius
    print('周长：%.2f' % perimeter)
    print('面积：%.2f' % area)

def leap_year():
    year = int(input('请输入年份：'))
    is_leap = (year % 4 == 0 and yaer % 100 != 0 or year % 400 == 0)
    print(is_leap)

if __name__ == '__main__':
    Fahrenheit_to_Celsius()
    cycle()
    leap_year()