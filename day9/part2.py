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


def sum_num(num, idx, array):
    start_idx = idx
    value = 0
    while(idx < len(array)):
        if value == num:
            return array[start_idx:idx]
        if value > num:
            return []
        value += array[idx]
        idx += 1
    return []


def find_contiguous(num, array):
    for (idx,_) in enumerate(array):
        nums = sum_num(num, idx, array)

        if (len(nums) != 0):
            nums = sorted(nums)
            print(f'result = {nums[0] + nums[len(nums) - 1]}')
            break


data = parse()

preamble = 25
for (index, num) in enumerate(data):
    if index >= preamble:
        if find_number(data[index - preamble: index], num) is False:
            print(f'result = {num}')
            find_contiguous(num, data)
            break
