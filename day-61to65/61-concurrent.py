import concurrent.futures
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

def is_prime(num):
    assert num > 0
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return num != 1

def multi_processing_test():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(f'{number} is prime: {prime}')

import asyncio

async def fetch(host):
    print(f'Start fetching {host}\n')
    reader, writer = await asyncio.open_connection(host, 80)
    writer.write(b'GET / HTTP/1.1\r\n')
    writer.write(f'Host: {host}\r\n'.encode())
    writer.write(b'\r\n')
    await writer.drain()
    line = await reader.readline()
    while line != b'\r\n':
        print(line.decode().rstrip())
        line = await reader.readline()
    print('\n')
    writer.close()

def asyncio_test():
    urls = ('www.sohu.com', 'www.douban.com', 'www.163.com')
    loop = asyncio.get_event_loop()
    tasks = [fetch(url) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    #multi_processing_test()
    asyncio_test()