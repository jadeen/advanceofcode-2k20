def read_files():
    f = open("input.txt")

    input = f.read()

    return input.split('\n')


def parse():
    lines = read_files()
    data = []

    for line in lines:
        data.append(int(line))
    return data


def find_number(array, num):
    for num1 in array:
        for num2 in array:
            if num1 + num2 == num:
                return True
    return False


data = parse()

preamble = 25
for (index, num) in enumerate(data):
    if index >= preamble:
        if find_number(data[index - preamble: index], num) is False:
            print(f'result = {num}')
            break
