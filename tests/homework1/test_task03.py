import os

from homework1.task03 import find_maximum_and_minimum


def test_positive_find_maximum_and_minimum():
    assert find_maximum_and_minimum(
        os.getcwd() + "/tests/homework1/min_max_test1.txt"
    ) == (-40, 15)


def test_positive_find_maximum_and_minimum2():
    print(os.getcwd())
    assert find_maximum_and_minimum(
        os.getcwd() + "/tests/homework1/min_max_test2.txt"
    ) == (-3, -3)
