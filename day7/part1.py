import re

f = open("input.txt")

input = f.read()

raws = input.split('\n')

bag_re = re.compile('([0-9]*)([a-z ]*)')


def parse(raws):
    bags = {}

    for raw in raws:
        bag = raw.split('contain')[0]
        contains = []

        for contain in raw.split('contain')[1].split(','):
            contain = contain.strip()

            if contain.strip() != "no other bags.":
                search = bag_re.search(contain)

                name = search.group(2).strip()
                contains.append({
                    "name": name if name[-1] == 's' else f'{name}s',
                    "value": int(search.group(1), 10),
                    "visited": False
                })

        bags[bag.strip()] = contains
    return bags


bags = parse(raws)

checked_bags = []


def found_bag(name):
    value = 0

    for bag in bags.get(name):
        if (bag.get('name') == 'shiny gold bags'):
            return True

        if found_bag(bag.get('name')) is True:
            return True

    return False


result = 0

for key in bags.keys():
    if found_bag(key) is True:
        result += 1

print(f'result = {result}')
