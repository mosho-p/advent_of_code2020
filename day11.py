from itertools import product

with open('inputs/day11_input.txt') as f:
    s = f.read().strip()

previous = []
current = [['L']*(len(s.split()[0])+2)] + [['L'] + list(x) + ['L'] for x in s.split()] + [['L']*(len(s.split()[0])+2)]
buffer = [[x for x in y] for y in current]

def find_seats(l, i, j):
    peeps = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x==0 and y==0:
                continue
            chair = l[i+x][j+y]
            loop = 1
            while chair == '.':
                loop += 1
                chair = l[i + x*loop][j + y*loop]
            if chair == '#':
                peeps += 1
    return peeps



while current != previous:
    for i in range(1, len(current)-1):
        for j in range(1, len(current[0])-1):
            if current[i][j] == '.':
                continue
            surrounding = find_seats(current, i, j)
            if current[i][j] == 'L' and not surrounding:
                buffer[i][j] = '#'
                continue
            if current[i][j] == '#' and surrounding > 4:
                buffer[i][j] = 'L'
    q=0
    previous = [[x for x in y] for y in current]
    current = [[x for x in y] for y in buffer]


answer = ''.join([''.join(x) for x in current])
print(answer.count('#'))



