from homework1.task04 import check_sum_of_four


def test_positive_check_sum_of_four():
    assert check_sum_of_four([4, 3], [-1, -5], [0, 1], [0, 1]) == 3


def test_negative_check_sum_of_four():
    assert check_sum_of_four([2, 2], [0, 0], [3, 3], [4, 4]) == 0


def test_positive_check_sum_of_four2():
    assert check_sum_of_four([0, 0], [0, 0], [0, 0], [0, 0]) == 16
