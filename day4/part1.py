f = open("input.txt")

input = f.read()

lines = input.split('\n')

papers = ['']
index = 0

for line in input.split('\n'):
    if len(line) == 0:
        papers.append('')
        index += 1
    else:
        papers[index] = line if len(
            papers[index]) == 0 else f'{papers[index]} {line}'

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def validate_passport(line):
    for field in required_fields:
        if field not in line:
            return False

    return True


valid = 0
for paper in papers:
    if validate_passport(paper):
        valid += 1

print(f'result = {valid}')
