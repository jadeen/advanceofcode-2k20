f = open("input.txt")

input = f.read()

raws = input.split('\n')


def get_id(raw):
    line = raw[:-3]
    line_bin = ''
    seat = raw.replace(line, '')
    seat_bin = ''

    for index, value in enumerate(line):
        if line[index] == 'F':
            line_bin += '0'
        else:
            line_bin += '1'

    for index, value in enumerate(seat):
        if line[index] == 'R':
            seat_bin += '0'
        else:
            seat_bin += '1'

    return int(line_bin, 2) * 8 + int(seat_bin, 2)


highId = 0
for raw in raws:
    id = get_id(raw)

    print(id, highId)

    if (id > highId):
        highId = id

print(f'result = {highId}')
