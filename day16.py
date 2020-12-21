import pandas as pd
from functools import reduce


with open('./inputs/day16_input.txt') as f:
    s = f.read().strip()

# Get valid numbers
rules, my_ticket, other_tickets = s.split('\n\n')
my_ticket = my_ticket.split('\n')[1]
my_ticket = [int(x) for x in my_ticket.split(',')]
other_tickets = other_tickets.partition('\n')[2]
valid_ranges = rules.split('\n')
valid_ranges = [s.split(': ')[1] for s in valid_ranges]
valid_ranges = [s.split(' or ')[0] for s in valid_ranges] + [s.split(' or ')[1] for s in valid_ranges]
valid_nums = set()
for ranges in valid_ranges:
    a, b = ranges.split('-')
    valid_nums.update(set(range(int(a), int(b)+1)))

# Check all numbers in "nearby tickets"
ticket_nums = [int(x) for x in other_tickets.replace('\n', ',').split(',')]
print(sum([int(x) for x in ticket_nums if x not in valid_nums]))

req = {}
for rule in rules.split('\n'):
    name, vals = rule.split(': ')
    r1, r2 = vals.split(' or ')
    r1a, r1b = r1.split('-')
    r2a, r2b = r2.split('-')
    r1a, r2a, r1b, r2b = list(map(int, [r1a, r2a, r1b, r2b]))
    req[name] = set(range(r1a, r1b+1)) | set(range(r2a, r2b+1))

df = pd.DataFrame([ticket.split(',') for ticket in other_tickets.split('\n') if all([int(x) in valid_nums for x in ticket.split(',')])]).astype(int)

departure_vals = []
for i in range(len(my_ticket)):
    for k, v in req.items():
        if 'depart' not in k:
            continue
        invalid = (set(df[i]) - v)
        if not invalid:
            departure_vals.append(my_ticket[i])
            break

print(departure_vals)
print(reduce(lambda a, b: a*b, departure_vals))

# TODO: Remove invalid tickets