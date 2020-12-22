from pathlib import Path
from typing import Tuple, Iterable

import more_itertools

realfile = Path(r'/Users/andrewmagerman/sourcecontrol/advent2020/src/day5/puzzleinput.txt')


def row_rec_magic(row_definitions: str, r: Iterable):
    front, back = more_itertools.divide(2, r)
    if len(row_definitions) == 1:
        if row_definitions == ['F']:
            return next(front)
        elif row_definitions == ['B']:
            return next(back)

    head, *tail = row_definitions

    if head == 'F':
        return row_rec_magic(tail, front)
    elif head == 'B':
        return row_rec_magic(tail, back)


def column_rec_magic(column_definition, r: Iterable):
    left, right = more_itertools.divide(2, r)
    if len(column_definition) == 1:
        if column_definition == ['L']:
            return next(left)
        elif column_definition == ['R']:
            return next(right)

    head, *tail = column_definition

    if head == 'L':
        return column_rec_magic(tail, left)
    elif head == 'R':
        return column_rec_magic(tail, right)


def row_column_seatid(param: str) -> Tuple[int, int, int]:
    row_definitions = param[:7]
    column_definition = param[-3:]

    row = row_rec_magic(row_definitions, range(0, 128))

    column = column_rec_magic(column_definition, range(0, 8))

    seat_id = row * 8 + column

    return row, column, seat_id


def read_lines_input(filepath: Path):
    with filepath.open('r') as f:
        a = f.read().splitlines()
        for l in a:
            yield l


def max_seat_id():
    return max(all_seat_ids())


def all_seat_ids():
    result = list()
    a = read_lines_input(realfile)
    for x in a:
        row, column, seat_id = row_column_seatid(x)
        result.append(seat_id)
    return result


def my_seat_id():
    a = all_seat_ids()
    for t in range(80, max(a) + 1):
        if t - 1 in a:
            if t + 1 in a:
                if t not in a:
                    return t


if __name__ == '__main__':
    print(max_seat_id())
    print(my_seat_id())
