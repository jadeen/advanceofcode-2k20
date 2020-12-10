import pprint
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
        if value == 'R':
            seat_bin += '1'
        else:
            seat_bin += '0'

    seat = int(seat_bin, 2)
    line = int(line_bin, 2)
    return {"id": int(line_bin, 2) * 8 + int(seat_bin, 2), "line": line, "seat": seat}

ids = {}
for raw in raws:
    obj = get_id(raw)

    ids[obj.get('id')] = obj
sorted_ids = sorted(ids)


start_id = sorted_ids[0]
end_id = sorted_ids[len(sorted_ids) - 1]

while start_id < 919:
    if ids.get(start_id, None) is None:
        print(f"result = {start_id}")
    start_id += 1