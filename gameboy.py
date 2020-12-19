class GameBoyError(Exception):
    def __init__(self, accumulator):
        self.accumulator = accumulator

    def __str__(self):
        return f'Accumulator at {self.accumulator}'


class LoopError(GameBoyError):
    pass


class ExitCode(GameBoyError):
    pass


class GameBoy:
    LoopError = LoopError
    ExitCode = ExitCode

    def __init__(self, rules):
        self.acc = 0
        self.rules = rules[:]
        self.index = 0
        self.read = [0] * len(rules)

    def run(self):
        self._validate_rule()
        self.read[self.index] = 1
        code, val = self.rules[self.index].split()
        val = int(val)
        self.execute(code, val)

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
            raise ExitCode(self.acc)
        if self.read[self.index] == 1:
            raise LoopError(self.acc)
