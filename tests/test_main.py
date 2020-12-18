from src.day1.main import entries_that_add_up_to_2020, sum_set_members, entries_that_add_up_to_2020_v2

expense_report = [1721,
                  979,
                  366,
                  299,
                  675,
                  1456]


def test_day1_1():
    assert entries_that_add_up_to_2020(expense_report) == {1721, 299}


def test_day1_2():
    assert entries_that_add_up_to_2020_v2(expense_report) == {979, 366, 675}


def test_day1_3():
    assert sum_set_members(entries_that_add_up_to_2020(expense_report)) == 514579


