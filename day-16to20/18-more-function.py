"""
Day 18
更多的函数
"""

from functools import wraps
from time import time, sleep

def record_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        print(func.__name__, time() - start_time)
        return result
    return wrapper

@record_time
def f(x, y):
    result = 1
    for x in range(y):
        result *= x - y
    sleep(4.5)
    return result

if __name__ == '__main__':
    item1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
    item2 = [x ** 2 for x in range(1, 10) if x % 2]
    print(item1, item2)

    print(f(45, 55))