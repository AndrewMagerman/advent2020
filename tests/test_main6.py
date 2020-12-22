from src.day6.main import *


def test_count_groups():
    assert len(groups(testfile)) == 5


grps = groups(testfile)


def test_sum_yes():
    assert sum_yes(grps[0]) == 3
    assert sum_yes(grps[1]) == 3
    assert sum_yes(grps[2]) == 3
    assert sum_yes(grps[3]) == 1
    assert sum_yes(grps[4]) == 1


def test_sum_all_yeses():
    assert sum_all_yeses(testfile) == 11


def test_everyone_answers_yes_same_question():
    assert sum_yes_same_question(grps[0]) == 3
    assert sum_yes_same_question(grps[1]) == 0
    assert sum_yes_same_question(grps[2]) == 1
    assert sum_yes_same_question(grps[3]) == 1
    assert sum_yes_same_question(grps[4]) == 1


grpsreal = groups(realfile)

def test_realfile():
    assert sum_yes_same_question(grpsreal[0]) == 1


def test_sum_agreements():
    assert sum_all_agreements(testfile) == 6

def test_answers_per_person():
    assert answers_per_person_in_group(grps[0]) == [{'c', 'b', 'a'}]
    assert answers_per_person_in_group(grps[1]) == [{'c'}, {'b'}, {'a'}]