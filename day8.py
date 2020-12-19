class GameBoy:
    def __init__(self, rules):
        self.acc = 0
        self.rules = rules[:]
        self.index = 0
        self.read = [0] * len(rules)

    def run(self):
        invalid = self._validate_rule()
        if invalid:
            return invalid
        self.read[self.index] = 1
        code, val = self.rules[self.index].split()
        val = int(val)
        self.execute(code, val)
        return ''

    def execute(self, code, val):
        if code == 'acc':
            self.index += 1
            self.acc += val
        elif code == 'nop':
            self.index += 1
        else:
            self.index += val

    def _validate_rule(self):
        if self.index >= len(self.rules):
            return f'Exit code {self.acc}'
        if self.read[self.index] == 1:
            return f'LoopError {self.acc}'


with open('inputs/day8_input.txt') as f:
    s = f.read().strip()
rules = s.split('\n')

# Part 1
gb = GameBoy(rules)
error = ''
while not error:
    error = gb.run()
print(error)

# Part 2
for i, rule in enumerate(rules):
    error = ''
    new_rules = rules[:]
    code, val = rule.split()
    if code == 'acc':
        continue
    elif code == 'nop':
        new_rules[i] = f'jmp {val}'
    else:
        new_rules[i] = f'nop {val}'
    gb = GameBoy(new_rules)

    while not error:
        error = gb.run()
    if 'Exit' in error:
        print(error)
        break
