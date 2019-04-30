"""
Day 20
并发
"""

def fib(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a+b
        yield a
class Fib(object):
    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.index += 1
            return self.a
        raise StopIteration()

import glob
import os
import threading
from PIL import Image
def generate_thumbnail(infile, size, format='PNG'):
    file, ext = os.path.splitext(infile)
    file = file[file.rfind(os.path.sep)+1:]
    outfile = f'./res/{file}_{size[0]}_{size[1]}{ext}'
    img = Image.open(infile)
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(outfile, format)
def thumbnail_test():
    if not os.path.exists('thumbnail'):
        os.mkdir('thumbnail')
    for infile in glob.glob('./res/*.png'):
        for size in (32, 64, 128):
            threading.Thread(
                target=generate_thumbnail,
                args=(infile, (size, size))
            ).start()

import time
from random import randint
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
class Account(object):
    def __init__(self):
        self.balance = 0.0
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
    def withdraw(self, money):
        with self.condition:
            while money > self.balance:
                self.condition.wait()
            new_balance = self.balance - money
            time.sleep(0.001)
            self.balance = new_balance
    def deposit(self, money):
        with self.lock:
            new_balance = self.balance + money
            time.sleep(0.001)
            self.balance = new_balance
            self.condition.notify_all()
class AddMoneyThread(threading.Thread):
    def __init__(self, account, money):
        self.account = account
        self.money = money
        super().__init__()
    def run(self):
        self.account.deposit(self.money)
def add_money(account):
    while True:
        money = randint(5, 10)
        account.deposit(money)
        print(f'{threading.current_thread().name}: {money} ===> {account.balance}')
        time.sleep(0,5)
def sub_money(account):
    while True:
        money = randint(5, 10)
        account.withdraw(money)
        print(f'{threading.current_thread().name}: {money} <=== {account.balance}')
        time.sleep(0.5)
def bank_test():
    account = Account()
    pool = ThreadPoolExecutor(max_workers=10)
    futures = []
    for _ in range(100):
        future = pool.submit(account.deposit, 1)
        futures.append(future)
    pool.shutdown()
    for future in futures:
        future.result()
    print(account.balance)
def bank_test2():
    account = Account()
    with ThreadPoolExecutor(max_workers = 10) as pool:
        for _ in range(5):
            pool.submit(add_money, account)
            pool.submit(sub_money, account)

import math
PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
] * 5
def is_prime(n):
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n+1, 2):
        if n % i == 0:
            return False
    return True
def prime_test():
    with ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(f'{number} is prime: {prime}')

import asyncio
def num_generator(m, n):
    yield from range(m, n+1)
async def prime_filter(m, n):
    primes = []
    for i in num_generator(m, n):
        flag = True
        for j in range(2, int(i ** 0.5 + 1)):
            if i % j == 0:
                flag = False
                break
        if flag:
            print(f'Prime => {i}')
            primes.append(i)
        await asyncio.sleep(0.001)
    return tuple(primes)
async def square_mapper(m, n):
    squares = []
    for i in num_generator(m, n):
        print(f'Square => {i * i}')
        squares.append(i * i)
        await asyncio.sleep(0.001)
    return squares
def async_test():
    loop = asyncio.get_event_loop()
    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
    future.add_done_callback(lambda x: print(x.result()))
    loop.run_until_complete(future)
    loop.close()

import re
import aiohttp
PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')
async def fetch_page(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()
async def show_title(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        print(PATTERN.search(html).group('title'))
def aiohttp_test():
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    loop = asyncio.get_event_loop()
    tasks = [show_title(url) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == '__main__':
    #thumbnail_test()
    #bank_test()
    #bank_test2()
    #prime_test()
    #async_test()
    aiohttp_test()
