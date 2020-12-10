import math
f = open("input.txt")

input = f.read()

lines = input.split('\n')

number_repeator = math.ceil(len(lines) / len(lines[0])) * 10

plan = [line * number_repeator for line in lines]

stop_point = len(lines) - 1


def navigate(move_x, move_y, stop_point, pla):
    x = 0
    y = 0

    see_three = 0

    while 1:
        x += move_x
        y += move_y

        if y > stop_point:
            break

        if plan[y][x] == '#':
            see_three += 1
    print(f'see_three = {see_three}')
    return see_three


result = navigate(1, 1, stop_point, plan)
result *= navigate(3, 1, stop_point, plan)
result *= navigate(5, 1, stop_point, plan)
result *= navigate(7, 1, stop_point, plan)
result *= navigate(1, 2, stop_point, plan)

print(f'result = {result}')
