#!/usr/bin/python3

for letters in range(122, 96, -1):
    if letters % 2:
        letters = letters - 32
    print("{:c}".format(letters), end='')
