import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


def read_lines_input(filepath: Path):
    with filepath.open('r') as f:
        a = f.read().splitlines()
        for l in a:
            yield l


def count_valid_passwords(filepath: Path):
    result = 0
    a = read_lines_input(filepath)
    for f in a:
        e = PassWordRule(f)
        if e.is_valid_2():
            result += 1
    return result


@dataclass
class PassWordRule:
    min: int = 0
    max: int = 0
    letter: str = ''
    password: str = ''

    def __init__(self, inputstr: str):
        m = re.match(r'(\d+)-(\d+) (\w): (\w+)', inputstr)
        if m:
            self.min = int(m.group(1))
            self.max = int(m.group(2))
            self.letter = m.group(3)
            self.password = m.group(4)

    def count_letter_in_password(self):
        b = Counter(self.password)

        return b[self.letter]

    def is_valid(self):
        return self.min <= self.count_letter_in_password() <= self.max

    def is_valid_2(self):
        return bool(self.letter_is_at_min()) ^ bool(self.letter_is_at_max())

    def letter_is_at_min(self):
        return self.password[self.min -1] == self.letter

    def letter_is_at_max(self):
        return self.password[self.max - 1] == self.letter

if __name__ == '__main__':
    print(count_valid_passwords(Path(r'/Users/andrewmagerman/sourcecontrol/advent2020/src/day2/puzzleinput.txt')))