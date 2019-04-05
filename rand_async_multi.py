#!/usr/bin/env python3

import string
import random
import asyncio

async def call_rand():
    await rand()

async def rand(n=4096):
    # string.printable = 
    # '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

    random_str = "".join(
            [
                random.choice(string.ascii_letters + string.punctuation) for i in range(n)])
    print(random_str)
    return None

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # コルーチン1個
    #loop.run_until_complete(call_rand())

    tasks = asyncio.wait([rand(int(i)) for i in range(1, 10000)])
    loop.run_until_complete(tasks)
    loop.close()
    print("----end----")


