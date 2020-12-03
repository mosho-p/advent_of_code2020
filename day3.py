def skiing(right, down):
    with open('inputs/day3_input.txt') as f:
        trees = 0
        for i, line in enumerate(f.readlines()):
            if i % down != 0:
                continue
            l = line.strip()
            if l[(i//down * right) % len(l)] == '#':
                trees += 1
    return trees


print(f'Part 1: {skiing(3, 1)}')
print(f'Part 2: {skiing(1, 1) * skiing(3, 1) * skiing(5, 1) * skiing(7, 1) * skiing(1, 2)}')
