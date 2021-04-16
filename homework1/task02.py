"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    is_fib_sequence = True
    fib_first = 0
    fib_second = 1
    if len(data) >= 3 and data[0] == fib_first and data[1] == fib_second:
        for index in range(len(data) - 3):
            if data[index] + data[index + 1] == data[index + 2]:
                index += 1
            else:
                is_fib_sequence = False
                break
    else:
        is_fib_sequence = False
    return is_fib_sequence
