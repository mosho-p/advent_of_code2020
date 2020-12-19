with open('inputs/day13_input.txt') as f:
    s = f.read().strip()

arrival = int(s.split()[0])
buses = list(map(int, s.replace('x,', '').split()[1].split(',')))

print(list(zip(list(map(lambda x: x*(arrival//x) + x - arrival, buses)), buses)))

buses = list(map(int, s.replace('x,', '1,').split()[1].split(',')))

x = 0
while True:
    x += buses[0]
    for i, bus in enumerate(buses):
        if (x + i) % bus != 0:
            break
    else:
        break

print(x)

# buses2 = []
# for i, bus in enumerate(buses):
#     buses2.append()

bus_prod = 1
for x in buses:
    bus_prod *= x
