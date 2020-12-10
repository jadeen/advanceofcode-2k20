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
    low = obj.get('low')
    max = obj.get('max')
    letter = obj.get('letter')
    password = obj.get('password')

    if password[low - 1] is letter and password[max - 1] is not letter:
        return True
    if password[low - 1] is not letter and password[max - 1] is letter:
        return True

    return False


f = open("input.txt")

input = f.read()

passwords = [parse(raw) for raw in input.split('\n')]

validePassword = 0

for password in passwords:
    if test(password):
        validePassword += 1

print(f'result:{validePassword}')
