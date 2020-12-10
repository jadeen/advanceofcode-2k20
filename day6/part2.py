f = open("input.txt")

input = f.read()

raws = input.split('\n')

groups = []
group = []

for raw in raws:
    if len(raw) == 0:
        groups.append(group)
        group = []
    else:
        group.append(raw)


def valid_question_people(answers, people):
    new_answers = []

    for answer in answers:
        if answer in people:
            new_answers.append(answer)
    return new_answers


result = 0

for peoples in groups:
    answers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for people in peoples:
        answers = valid_question_people(answers, people)

    result += len(answers)

print(f'result = {result}')


    
