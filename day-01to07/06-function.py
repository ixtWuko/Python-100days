"""
Day 6
函数

Author: ixtwuko
"""

def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
def lcm(x, y):
    return x * y // gcd(x, y)

def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False

if __name__ == '__main__':
    print('计算两个整数的最大公约数和最小公倍数')
    x = int(input('请输入第一个整数：'))
    y = int(input('请输入第二个整数：'))
    print('%d和%d的最大公约数为%d' %(x, y, gcd(x, y)))
    print('%d和%d的最小公倍数为%d' %(x, y, lcm(x, y)))

    print('判定一个整数是否为回文数')
    num = int(input('请输入一个整数：'))
    print(is_palindrome(num))

    print('判定一个整数是否为素数')
    num = int(input('请输入一个整数：'))
    print(is_prime(num))