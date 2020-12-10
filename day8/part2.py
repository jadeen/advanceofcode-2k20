import numpy as np
import copy


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

    while idx < len(process):
        instru = process[idx]

        if instru.get('visited') is True:
            raise "nope"

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


def alterne_process(process, idx):
    copy_process = copy.deepcopy(process)
    for (vIdx, value) in enumerate(process):
        command = value.get('command')

        if command == 'nop' and vIdx >= idx:
            copy_process[vIdx]['command'] = 'jmp'
            return (copy_process, vIdx)

        if command == 'jmp' and vIdx >= idx:
            copy_process[vIdx]['command'] = 'nop'
            return (copy_process, vIdx)

    raise "Looser"


def clean_process(proccess):
    for value in process:
        value['visited'] = False
    return process

process = parser()

idx = 0

while True:
    (changed_process, idx) = alterne_process(process, idx)

    try:
        print(f'result = {exec(changed_process)}')
        break
    except:
        idx += 1
