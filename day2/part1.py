#!/usr/bin/env python

def parse(raw):
    raw = raw.split(' ')
    return {
        "low": int(raw[0].split('-')[0]),
        "max": int(raw[0].split('-')[1]),
        "letter": raw[1][0],
        "password": raw[2],
    }


def test(obj):
    count = 0

    for letter in obj.get('password'):
        if letter is obj.get('letter'):
            count += 1

    return True if count >= obj.get('low') and count <= obj.get('max') else False


f = open("input.txt")

input = f.read()

passwords = [parse(raw) for raw in input.split('\n')]

validePassword = 0

for password in passwords:
    if test(password):
        validePassword += 1

print(f'result:{validePassword}')
