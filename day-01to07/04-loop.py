"""
Day 4
循环

Author: ixtwuko
"""

import math

def prime_number():
    num = int(input('请输入一个整数：'))
    end = int(math.sqrt(num))
    is_prime = True
    for x in range(2, end+1):
        if num % x == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        print('%d是素数' % num)
    else:
        print('%d不是素数' % num)

def common_number():
    x = int(input('x = '))
    y = int(input('y = '))
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            print('%d和%d的最大公约数是%d' % (x, y, factor))
            print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
            break

def print_triangle():
    character = input('请输入字符：')
    row = int(input('请输入行数：'))
    for i in range(row):
        for _ in range(i + 1):
            print(character, end = '')
        print()
    for i in range(row):
        for j in range(row):
            if j < row - i - 1:
                print(' ', end = '')
            else:
                print(character, end = '')
        print()
    for i in range(row):
        for _ in range(row - i - 1):
            print(' ', end = '')
        for _ in range(2 * i + 1):
            print(character, end = '')
        print()

if __name__ == '__main__':
    prime_number()
    common_number()
    print_triangle()