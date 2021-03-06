from itertools import product

with open('inputs/day14_input.txt') as f:
    s = f.read().strip()

rules = s.split('\n')
mem = {}
mask = ''

for rule in rules:
    if rule[:3] == 'mas':
        mask = rule.split(' = ')[1]
        continue
    a, b, c = rule.partition(' = ')
    c = str(bin(int(c)))[2:].zfill(36)
    c = ''.join([a if b=='X' else b for a, b in zip(c, mask)])
    a = a.replace('mem[', '').replace(']', '')
    mem[a] = c


print(sum([int(x, 2) for x in mem.values()]))


mem = {}
mask = ''

for rule in rules:
    if rule[:3] == 'mas':
        mask = rule.split(' = ')[1]
        continue
    address_int, value = rule.split(' = ')
    address_int = address_int.replace('mem[', '').replace(']', '')
    result = str(bin(int(address_int)))[2:].zfill(36)
    result = ''.join([max([a, b]) for a, b in zip(result, mask)])
    base = int(result.replace('X', '0'), 2)
    wilds = [2**(i) for i, x in enumerate(result[::-1], 0) if x == 'X']
    locations = []
    for coefs in product('01', repeat=len(wilds)):
        locations.append(base + sum([a*int(b) for a, b in zip(wilds, coefs)]))
    for l in locations:
        mem[l] = int(value)

print(sum(mem.values()))