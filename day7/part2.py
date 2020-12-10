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
                "name": name if name[-1] == 's' else f'{name}s' ,
                "value": int(search.group(1), 10),
                "visited": False
              })

        bags[bag.strip()] = contains
    return bags


bags = parse(raws)

checked_bags = []

def found_bag(name):
    value = 0

    if len(bags.get(name)) == 0:
        return 1

    for bag in bags.get(name):
        result = found_bag(bag.get('name'))
        if result >= 1:
          value += bag.get('value') * result
        if result > 1:
          value += bag.get('value')

    return value

result = 0

for bag in bags.get('shiny gold bags'):
    result += bag.get('value')
    result += bag.get('value') * found_bag(bag.get('name'))
print(f"result = {found_bag('shiny gold bags')}")