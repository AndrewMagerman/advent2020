from dataclasses import dataclass
from pathlib import Path
from typing import List

testfile = Path(r'/Users/andrewmagerman/sourcecontrol/advent2020/src/day3/testinput.txt')
realfile = Path(r'/Users/andrewmagerman/sourcecontrol/advent2020/src/day3/puzzleinput.txt')


@dataclass
class Slope:
    right: int
    down: int


slopes = [Slope(right=1, down=1),
          Slope(right=3, down=1),
          Slope(right=5, down=1),
          Slope(right=7, down=1),
          Slope(right=1, down=2),
          ]


@dataclass
class Point:
    row: int
    column: int


def read_position(file: Path, p: Point):
    array = list()
    with file.open('r') as f:
        a = f.read().splitlines()
        for line in a:
            array.append(line * 5000)
            # print(line * 10)
    line = array[p.row]
    result = line[p.column]
    return result


def hastree(testfile: Path, param: Point):
    return read_position(testfile, param) == '#'


def trajectory(slope: Slope):
    row = 0
    column = 0

    yield Point(row, column)
    while True:
        row += slope.down
        column += slope.right
        yield Point(row, column)


def count_trees(file: Path, slope: Slope):
    t = trajectory(slope)
    result = 0
    try:
        while True:
            if hastree(file, next(t)):
                result += 1
                print(result)
    finally:
        return result


def prod_1(file: Path, slopes: List[Slope]):

    result = 1
    for slope in slopes:
        result = result * count_trees(file, slope)
    return result


if __name__ == '__main__':
    print(prod_1(realfile, slopes))
