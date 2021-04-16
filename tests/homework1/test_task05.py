from homework1.task05 import find_maximal_subarray_sum


def test_positive_find_maximal_subarray_sum():
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test_positive_find_maximal_subarray_sum2():
    assert find_maximal_subarray_sum([0, 5, -1, -3, -4, 1, 8, 11, -4, -5], 4) == 20


def test_positive_find_maximal_subarray_sum3():
    assert find_maximal_subarray_sum([-2, -5, -6, -8], 1) == -2
