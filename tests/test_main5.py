from src.day5.main import *


def test_value_is_four_digits_and_in_range():
    assert row_column_seatid('FBFBBFFRLR') == (44, 5, 357)
    assert row_column_seatid('BFFFBBFRRR') == (70, 7, 567)
    assert row_column_seatid('FFFBBBFRRR') == (14, 7, 119)
    assert row_column_seatid('BBFFBBFRLL') == (102, 4, 820)


def test_column_magic():
    column_range = range(0, 8)
    assert column_rec_magic('RLR', column_range) == 5


def test_row_magic():
    assert row_rec_magic('FBFBBFF', range(0, 128)) == 44
    assert row_rec_magic('BFFFBBF', range(0, 128)) == 70
