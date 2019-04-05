#!/usr/bin/env python3

import string
import random


def rand(n=10):
    # string.printable = 
    # '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

    random_str = "".join(
            [
                random.choice(string.ascii_letters + string.punctuation) for i in range(n)])

    return random_str

if __name__ == '__main__':
    print(rand(100000))

