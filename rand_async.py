#!/usr/bin/env python3

import string
import random
import asyncio

async def call_rand():
    await rand()

async def rand(n=10):
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
    loop.run_until_complete(call_rand())

    loop.close()
    print("----end----")

