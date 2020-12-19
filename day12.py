class Boat:
    def __init__(self):
        self.north = 0
        self.east = 0
        self.facing = 1
        self.compass = 'nesw'
        self.waypoint_north = 1
        self.waypoint_east = 10

    def n(self, x):
        self.waypoint_north += x

    def e(self, x):
        self.waypoint_east += x

    def s(self, x):
        self.waypoint_north -= x

    def w(self, x):
        self.waypoint_east -= x

    def l(self, x):
        for _ in range(x//90 % 4):
            self.waypoint_north, self.waypoint_east = self.waypoint_east, self.waypoint_north * -1

    def r(self, x):
        for _ in range(x // 90 % 4):
            self.waypoint_north, self.waypoint_east = self.waypoint_east * -1, self.waypoint_north

    def f(self, x):
        self.north += self.waypoint_north * x
        self.east += self.waypoint_east * x


with open('inputs/day12_input.txt') as f:
    s = f.read().strip().lower()
directions = [(direction[0], int(direction[1:])) for direction in s.split()]

boaty_mcboatface = Boat()
for action, value in directions:
    eval(f'boaty_mcboatface.{action}({value})')

print(abs(boaty_mcboatface.north) + abs(boaty_mcboatface.east))
