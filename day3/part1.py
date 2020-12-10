import math
f = open("input.txt")

input = f.read()

lines = input.split('\n')

number_repeator = math.ceil(len(lines) / len(lines[0])) * 3

plan = [line * number_repeator for line in lines]

stop_point = len(lines) - 1
x = 0
y = 0

see_three = 0

while 1:
    x += 3
    y += 1

    if y > stop_point:
        break

    if plan[y][x] is '#':
        see_three += 1
