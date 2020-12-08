with open('inputs/day6_input.txt') as f:
    questions = f.read().strip()

groups = questions.split('\n\n')

total = 0
for x in groups:
    answers = set('abcdefghijklmnopqrstuvwxyz')
    people = x.split()
    for person in people:
        answers = set(list(person)) & answers
    total += len(answers)

print(total)
