import re
from functools import partial
from pathlib import Path

testfile = Path(r'/Users/andrewmagerman/sourcecontrol/advent2020/src/day4/testinput.txt')
realfile = Path(r'/Users/andrewmagerman/sourcecontrol/advent2020/src/day4/puzzleinput.txt')


def value_is_four_digits_and_in_range(smallest, largest, param):

    if not re.match(r'\d{4}', param):
        return False

    return smallest <= int(param) <= largest


def hgt_is_valid(param):
    a = re.match(r'(\d+)(cm|in)', param)
    if not a:
        return False
    number, unit = int(a.group(1)), a.group(2)
    return {'cm': 150 <= number <= 193,
            'in': 59 <= number <= 76}[unit]


def ecl_is_valid(param):
    return param in 'amb blu brn gry grn hzl oth'.split()


rules = {'byr': partial(value_is_four_digits_and_in_range, 1920, 2002),
         'iyr': partial(value_is_four_digits_and_in_range, 2010, 2020),
         'eyr': partial(value_is_four_digits_and_in_range, 2020, 2030),
         'hgt': hgt_is_valid,
         'hcl': partial(re.match, r'#[0-9a-f]{6}'),
         'ecl': ecl_is_valid,
         'pid': partial(re.match, r'\d{9}$'),
         }


def passports(file: Path):
    with file.open('r') as f:
        return f.read().split('\n\n')


def fields(passport: str):
    result = dict()
    for entry in entries(passport):
        k = entry.partition(':')
        result[k[0]] = k[2]
    return result


def entries(passport: str):
    return passport.split()


def is_valid(passport):
    all_fields = fields(passport)

    for n in rules:
        if n not in all_fields:
            return False

    for key, value in all_fields.items():
        if key == 'cid':
            continue
        if not rules[key](value):
            return False

    return True


def count_valid_passports(file):
    result = 0
    for p in passports(file):
        if is_valid(p):
            result += 1

    return result


if __name__ == '__main__':
    print(count_valid_passports(realfile))
