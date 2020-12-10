import re

hair_re = re.compile('^#[0-9a-f]{6}$')
pid_re = re.compile('^[0-9]{9}$')

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


def parse_paper(raw):
    paper = {}

    for field in raw.split(' '):
        paper[field.split(':')[0]] = field.split(':')[1]

    return paper


def validate_passport_field(paper):
    # valid byr
    byr = int(paper.get('byr'))
    if byr < 1920 or byr > 2002:
        return False

    # valid iyr
    iyr = int(paper.get('iyr'))
    if iyr < 2010 or iyr > 2020:
        return False

    # valid eyr
    eyr = int(paper.get('eyr'))
    if eyr < 2020 or eyr > 2030:
        return False

    # valid hgt
    hgt = paper.get('hgt')
    print(hgt)
    size = int(hgt[:-2])

    if 'cm' not in hgt and 'in' not in hgt:
        print('invalid')
        return False
    if 'cm' in hgt and (size < 150 or size > 193):
        return False

    if 'in' in hgt and (size < 59 or size > 76):
        return False

    # valid hcl
    hcl = paper.get('hcl')
    if hair_re.match(hcl) is None:
        return False

    # valid ecl
    if paper.get('ecl') not in 'amb blu brn gry grn hzl oth':
        return False

    if pid_re.match(paper.get('pid')) is None:
        return False

    return True


valid = 0
for paper in papers:
    if validate_passport(paper) is True:
        paper = parse_paper(paper)
        if validate_passport_field(paper) is True:
            valid += 1

print(f'result = {valid}')
