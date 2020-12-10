#!/usr/bin/env python

f = open("input.txt")

input = f.read()

codes = [int(value) for value in input.split()]

for idx, code in enumerate(codes):
    for idx2, code2 in enumerate(codes):
        for idx3, code3 in enumerate(codes):
            if code + code3 + code2 == 2020:
                print(code * code2 * code3)
                exit()
