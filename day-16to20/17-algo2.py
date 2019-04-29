"""
Day 17
更多算法
"""

def chicken():
    """
    百钱百鸡：公鸡5元，母鸡3元，小鸡1元三只
    """
    for x in range(20):
        for y in range(33):
            z = 100 - x - y
            if 5 * x + 3 * y + z // 3 == 100 and z % 3 ==0:
                print(x, y, z)

def fish():
    """
    # A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
    # 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
    # B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
    # 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
    """
    fish = 1
    while True:
        total = fish
        enough = True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
        if enough:
            print(fish)
            break
        fish += 1

class Thing(object):
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        return self.price / self.weight

def things_test():
    """
    贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
    输入：
    20 6
    电脑 200 20
    收音机 20 4
    钟 175 10
    花瓶 50 2
    书 10 1
    油画 90 9
    """
    def input_thing():
        name_str, price_str, weight_str = input('输入：').split()
        return name_str, int(price_str), int(weight_str)
    max_weight, num_of_things = map(int, input('输入总量：').split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_price + thing.weight <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'总价值：{total_price}美元')

def quick_sort_test():
    def quick_sort(origin_items, comp=lambda x, y: x <= y):
        items = origin_items
        _quick_sort(items, 0, len(items) - 1, comp)
        return items
    def _quick_sort(items, start, end, comp):
        if start <= end:
            pos = _partition(items, start, end, comp)
            _quick_sort(items, start, pos-1, comp)
            _quick_sort(items, pos+1, end, comp)
    def _partition(items, start, end, comp):
        pivot = items[end]
        i = start - 1
        for j in range(start, end):
            if comp(items[j], pivot):
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i+1], items[end] = items[end], items[i+1]
        return i+1

    print(quick_sort([34, 25, 12, 99, 87, 63, 58, 78, 88, 92]))

import sys
import time
def backtracking_test():
    size = 5
    total = 0
    def print_board(board):
        for row in board:
            for col in row:
                print(str(col).center(4), end='')
            print()
    def patrol(board, row, col, step=1):
        if row >= 0 and row < size and col >= 0 and col < size and board[row][col] == 0:
            board[row][col] = step
            if step == size * size:
                nonlocal total
                total += 1
                print(f'第{total}种走法: ')
                print_board(board)
            patrol(board, row - 2, col - 1, step + 1)
            patrol(board, row - 1, col - 2, step + 1)
            patrol(board, row + 1, col - 2, step + 1)
            patrol(board, row + 2, col - 1, step + 1)
            patrol(board, row + 2, col + 1, step + 1)
            patrol(board, row + 1, col + 2, step + 1)
            patrol(board, row - 1, col + 2, step + 1)
            patrol(board, row - 2, col + 1, step + 1)
            board[row][col] = 0

    board = [[0] * size for _ in range(size)]
    patrol(board, size-1, size-1)

def fib(num, temp={}):
    if num in (1,2):
        return 1
    try:
        return temp[num]
    except KeyError:
        temp[num] = fib(num-1) + fib(num-2)
        return temp[num]

def max_sum_test():
    items = list(map(int, input('请输入数据：').split()))
    size = len(items)
    overall, partial = {}, {}
    overall[size-1] = partial[size-1] = items[size-1]
    for i in range(size-2, -1, -1):
        partial[i] = max(items[i], partial[i+1]+items[i])
        overall[i] = max(partial[i], overall[i+1])
    print(overall[0])

if __name__ == '__main__':
    chicken()
    fish()
    #things_test()
    quick_sort_test()
    #backtracking_test()
    print(fib(50))
    max_sum_test()