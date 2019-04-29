"""
Day 5
基础的练习
"""

def narcissistic_number():
    '''判定一个整数是否为水仙花数'''
    num = int(input('请输入一个整数：'))
    tmp = num
    length = len(str(tmp))
    sum = 0
    while tmp != 0:
        reminder = tmp % 10
        sum += reminder ** length
        tmp = tmp // 10
    if sum == num:
        print('%d是水仙花数' % (num))
    else:
        print('%d不是水仙花数' % (num))

def perfect_number():
    '''判定一个整数是否为完美数'''
    num = int(input('请输入一个整数：'))
    sum = 0
    for factor in range(1, num):
        if num % factor == 0:
            sum += factor
    if sum == num:
        print('%d是完美数' % (num))
    else:
        print('%d不是完美数' % (num))

def fibonacci():
    '''输出一定长度的斐波那契数列'''
    length = int(input('请输入斐波那契数列长度：'))
    a = 1
    b = 1
    print('%d %d' %(a, b), end = ' ')
    for _ in range(2, length):
        tmp = a + b
        print('%d' %(tmp), end = ' ')
        a = b
        b = tmp
    print()

if __name__ == '__main__':
    narcissistic_number()
    perfect_number()
    fibonacci()