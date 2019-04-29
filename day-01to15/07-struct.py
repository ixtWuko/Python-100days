"""
Day 7
数据结构
"""

import os
import time
def marquee():
    content = '在屏幕上显示跑马灯文字'
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]

import random
def generate_code(code_len = 4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars)
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code

def get_suffix(filename, has_dot = False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename):
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
def which_day(year, month, date):
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)] # WOW
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date

def yanghui_triangle():
    num = int(input('请输入行数：'))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row-1][col] + yh[row-1][col-1]
            print(yh[row][col], end='\t')
        print()

if __name__ == '__main__':
    #marquee()
    print(generate_code(6))
    print(get_suffix('readme.md'))

    x = [random.randint(10, 99) for i in range(30)]
    print(x)
    print(max2(x))

    print(which_day(2018, 3, 1))
    yanghui_triangle()
