def parse_pass(s):
    k, v = s.split(': ')
    num, char_ = k.split()
    min_, max_ = num.split('-')
    min_, max_ = int(min_), int(max_)
    return min_, max_, char_, v


def is_valid(s):
    min_, max_, char_, v = parse_pass(s)
    return min_ <= v.count(char_) <= max_


def is_now_valid(s):
    min_, max_, char_, v = parse_pass(s)
    if len(v) < max_:
        return v[min_ - 1] == char_
    return int(v[min_ - 1] == char_) + int(v[max_ - 1] == char_) == 1


with open('inputs/day2_input.txt') as f:
    passwords = f.read().strip().split('\n')

print(f'Part 1: {sum([1 for s in passwords if is_valid(s)])}')
print(f'Part 2: {sum([1 for s in passwords if is_now_valid(s)])}')
