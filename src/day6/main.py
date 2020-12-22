from collections import Counter
from pathlib import Path

testfile = Path(r'/Users/andrewmagerman/sourcecontrol/advent2020/src/day6/testinput.txt')
realfile = Path(r'/Users/andrewmagerman/sourcecontrol/advent2020/src/day6/puzzleinput.txt')


# Lessons learned: use splitlines() instead of split('\n')
# sets are really cool

def sum_yes(group: str):
    c = Counter()
    for question in group:
        if question == '\n':
            continue
        c[question] += 1
    return len(c)


def sum_all_yeses(file: Path):
    grps = groups(file)
    result = 0
    for group in grps:
        result += sum_yes(group)
    return result


def sum_all_agreements(file):
    grps = groups(file)
    result = 0
    for count, group in enumerate(grps):
        result += sum_yes_same_question(group)
        print(f'*** {count}')
        print(group)
        print(sum_yes_same_question(group))

    return result


def answers_per_person_in_group(group):
    result = list()
    persons = group.splitlines()
    for person in persons:
        answers_yes = set(person)
        result.insert(0, answers_yes)
    return result


def sum_yes_same_question(group):
    a = answers_per_person_in_group(group)
    head, *tail = a
    if tail:
        k = head.intersection(*tail)
    else:
        k = head
    return len(k)


def groups(file: Path):
    with file.open('r') as f:
        return f.read().split('\n\n')


if __name__ == '__main__':
    print(sum_all_agreements(realfile))
