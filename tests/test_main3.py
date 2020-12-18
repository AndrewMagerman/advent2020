from src.day3.main import *

s = Slope(right=3, down=1)
t = trajectory(s)


def test_read_lines_input():
    assert next(t) == Point(row=0, column=0)
    assert next(t) == Point(row=1, column=3)
    assert next(t) == Point(row=2, column=6)


def test_hastree_row_1():
    assert hastree(testfile, Point(row=0, column=0)) is False
    assert hastree(testfile, Point(row=1, column=3)) is False
    assert hastree(testfile, Point(row=2, column=6)) is True


def test_read_position():
    assert read_position(testfile, Point(row=0, column=0)) == '.'
    assert read_position(testfile, Point(row=2, column=6)) == '#'


def test_count_trees():
    assert count_trees(testfile, slopes[0]) == 2
    assert count_trees(testfile, slopes[1]) == 7
    assert count_trees(testfile, slopes[2]) == 3
    assert count_trees(testfile, slopes[3]) == 4
    assert count_trees(testfile, slopes[4]) == 2


def test_sum_slopes():
    assert prod_1(testfile, slopes) == 336

