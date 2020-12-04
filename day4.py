import re


# part one
required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
with open('inputs/day4_input.txt') as f:
    print(sum([set(field.split(':')[0] for field in passport.split()) >= required for passport in f.read().strip().split('\n\n')]))

# part two
with open('inputs/day4_input.txt') as f:
    passports = [{field.split(':')[0]: field.split(':')[1] for field in passport.split() if field.split(':')[0] != 'cid'} for passport in f.read().strip().split('\n\n') if set(field.split(':')[0] for field in passport.split()) >= required]

def byr(s):
    return bool(re.fullmatch(r'19[2-9][0-9]|200[0-2]', s))
def iyr(s):
    return bool(re.fullmatch(r'201[0-9]|2020', s))
def eyr(s):
    return bool(re.fullmatch(r'202[0-9]|2030', s))
def hgt(s):
    return bool(re.fullmatch(r'(59|6[0-9]|7[0-6])in|(1[5-8][0-9]|19[0-3])cm', s))
def hcl(s):
    return bool(re.fullmatch(r'#[0-9a-f]{6}', s))
def ecl(s):
    return s in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
def pid(s):
    return bool(re.fullmatch(r'[0-9]{9}', s))

print(sum([all([eval(f'{k}("{v}")') for k, v in passport.items()]) for passport in passports]))
