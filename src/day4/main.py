import re
from pathlib import Path

testfile = Path(r'/Users/andrewmagerman/sourcecontrol/advent2020/src/day4/testinput.txt')
realfile = Path(r'/Users/andrewmagerman/sourcecontrol/advent2020/src/day4/puzzleinput.txt')


def is_four_digits(value):
    if not len(value) == 4:
        return False
    if not re.match(r'\d{4}', value):
        return False
    return True


def byr_is_valid(value):
    if not is_four_digits(value):
        return False

    k = int(value)

    return 1920 <= k <= 2002


def iyr_is_valid(value):
    if not is_four_digits(value):
        return False

    k = int(value)

    return 2010 <= k <= 2020


def eyr_is_valid(value):
    if not is_four_digits(value):
        return False

    k = int(value)

    return 2020 <= k <= 2030


def hgt_is_valid(value):
    a = re.match(r'(\d+)(cm|in)', value)
    if not a:
        return False
    number = int(a.group(1))
    unit = a.group(2)
    if unit == 'cm':
        return 150 <= number <= 193
    if unit == 'in':
        return 59 <= number <= 76

    print(number, unit)
    return True


def hcl_is_valid(value):
    return re.match(r'#[0-9a-f]{6}', value)


def ecl_valid(param):
    valid_values = 'amb blu brn gry grn hzl oth'.split()
    return param in valid_values


def pid_valid(param):
    return re.match(r'\d{9}$', param)


rules = {'byr': byr_is_valid,
         'iyr': iyr_is_valid,
         'eyr': eyr_is_valid,
         'hgt': hgt_is_valid,
         'hcl': hcl_is_valid,
         'ecl': ecl_valid,
         'pid': pid_valid,
         }


def passports(file: Path):
    with file.open('r') as f:
        a = f.read()
        passports = a.split('\n\n')
        return passports


def fields(passport: str):
    result = dict()
    for entry in entries(passport):
        k = entry.partition(':')
        result[k[0]] = k[2]
    print(result)
    return result


def entries(passport: str):
    return passport.split()


def is_valid(passport):
    all_fields = fields(passport)
    print(all_fields)
    necesary_entries = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        # 'cid',
    ]
    for n in necesary_entries:
        if n not in all_fields:
            return False

    for key, value in all_fields.items():
        if key == 'cid':
            continue
        test_function = rules[key]
        if not test_function(value):
            return False

    return True


def count_valid_passports(testfile):
    result = 0
    pp = passports(testfile)
    for p in pp:
        if is_valid(p):
            result += 1

    return result


if __name__ == '__main__':
    print(count_valid_passports(realfile))
