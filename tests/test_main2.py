from pathlib import Path

from src.day2.main import read_lines_input, PassWordRule, count_valid_passwords

lines = read_lines_input(Path("/Users/andrewmagerman/sourcecontrol/advent2020/src/day2/testinput.txt"))
a = next(lines)
b = next(lines)
c = next(lines)


def test_1():
    assert a == "1-3 a: abcde"
    assert b == "1-3 b: cdefg"
    assert c == "2-9 c: ccccccccc"


pwra = PassWordRule(a)


def test_2():
    assert pwra.min == 1
    assert pwra.max == 3
    assert pwra.letter == 'a'
    assert pwra.password == 'abcde'
    assert pwra.is_valid() is True
    # assert pwra.is_valid_2() is True
    assert pwra.letter_is_at_min() is True
    assert pwra.letter_is_at_max() is False


pwrb = PassWordRule(b)


def test_22():
    assert pwrb.min == 1
    assert pwrb.max == 3
    assert pwrb.letter == 'b'
    assert pwrb.password == 'cdefg'
    assert pwrb.is_valid() is False
    assert pwrb.is_valid_2() is False


pwrc = PassWordRule(c)


def test_21():
    assert pwrc.min == 2
    assert pwrc.max == 9
    assert pwrc.letter == 'c'
    assert pwrc.password == 'ccccccccc'
    assert pwrc.is_valid() is True
    assert pwrc.is_valid_2() is False


def test_3():
    assert pwra.is_valid()


def test_4():
    assert pwra.count_letter_in_password() == 1


def test_5():
    assert count_valid_passwords(Path("/Users/andrewmagerman/sourcecontrol/advent2020/src/day2/testinput.txt")) == 1
