def get_seat_id(s):
    decimal_row = int(s[:-3].replace('B', '1').replace('F', '0'), 2)
    decimal_col = int(s[-3:].replace('R', '1').replace('L', '0'), 2)
    return decimal_row * 8 + decimal_col


with open('inputs/day5_input.txt') as f:
    raw = f.read()

seats = raw.strip().split()
seat_ids = list(map(get_seat_id, seats))

# Part 1
print(max(seat_ids))

# Part 2
for n in range(8, 127*8):
    if n not in seat_ids and n + 1 in seat_ids and n - 1 in seat_ids:
        print(n)
