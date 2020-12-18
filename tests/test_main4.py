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
    assert rules['byr']('200') is False
    assert rules['byr']('2002') is True
    assert rules['byr']('2003') is False


def test_hgt():
    assert hgt_is_valid('60in')
    assert hgt_is_valid('190cm')
    assert not hgt_is_valid('190in')
    assert not hgt_is_valid('190')


def test_hcl():
    assert rules['hcl']('#123abc')
    assert not rules['hcl']('#123abz')
    assert not rules['hcl']('123abc')


def test_ecl_valid():
    assert ecl_is_valid('brn')
    assert not ecl_is_valid('wat')


def test_pid():
    assert rules['pid']('000000001')
    assert not rules['pid']('0123456789')


def test_valid_passports():
    valid_passports = passports(Path(r'/Users/andrewmagerman/sourcecontrol/advent2020/src/day4/valid_passports.txt'))
    for p in valid_passports:
        assert is_valid(p)


def test_invalid_passports():
    valid_passports = passports(Path(r'/Users/andrewmagerman/sourcecontrol/advent2020/src/day4/invalid_passports.txt'))
    for p in valid_passports:
        assert not is_valid(p)
