f = open("input.txt")

input = f.read()

raws = input.split('\n')

groups = []
group = ''

for raw in raws:
    if len(raw) == 0:
        groups.append(group)
        group = ''
    else:
        group +=  raw

def valid_question_group(group):
    answers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    valid = 0

    for answer in answers:
        if answer in group:
            valid += 1
    return valid

result = 0



for group in groups:
    valid = valid_question_group(group)
    
    result += valid

print(f'result = {result}')


    
