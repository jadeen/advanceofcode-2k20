def read_files():
    f = open("input.txt")

    input = f.read()

    return input.split('\n')


def parser():
    raws = read_files()
    process = []

    for raw in raws:
        process.append({
            "command": raw.split(' ')[0],
            "value": int(raw.split(' ')[1]),
            "visited": False
        })
    return process


def exec(process):
    acc = 0
    idx = 0

    while True:
        instru = process[idx]

        if instru.get('visited') is True:
            break

        instru['visited'] = True
        command = instru.get('command')

        if command == 'acc':
            acc += instru.get('value')
            idx += 1

        if command == 'jmp':
            idx += instru.get('value')

        if command == 'nop':
            idx += 1

    return acc


process = parser()

print(f'result = {exec(process)}')
