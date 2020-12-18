from src.day4.main import *

pp = passports(testfile)

p0 = pp[0]
print(p0)


def test_count_passports():
    assert len(passports(testfile)) == 4


def test_fields():
    print(p0)
    assert fields(p0)['hcl'] == '#fffffd'


def test_is_valid():
    assert is_valid(p0)


def test_count_valid_passports():
    assert count_valid_passports(testfile) == 2


def test_byr():
    assert byr_is_valid('200') is False
    assert byr_is_valid('2002') is True
    assert byr_is_valid('2003') is False


def test_hgt():
    assert hgt_is_valid('60in')
    assert hgt_is_valid('190cm')
    assert not hgt_is_valid('190in')
    assert not hgt_is_valid('190')


def test_hcl():
    assert hcl_is_valid('#123abc')
    assert not hcl_is_valid('#123abz')
    assert not hcl_is_valid('123abc')


def test_ecl_valid():
    assert ecl_valid('brn')
    assert not ecl_valid('wat')


def test_pid():
    assert pid_valid('000000001')
    assert not pid_valid('0123456789')


def test_valid_passports():
    valid_passports = passports(Path(r'/Users/andrewmagerman/sourcecontrol/advent2020/src/day4/valid_passports.txt'))
    for p in valid_passports:
        assert is_valid(p)


def test_invalid_passports():
    valid_passports = passports(Path(r'/Users/andrewmagerman/sourcecontrol/advent2020/src/day4/invalid_passports.txt'))
    for p in valid_passports:
        assert not is_valid(p)
