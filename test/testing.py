import pytest


def func(num):
    return num * 2

def test_answer():
    assert func(6) == 10
    return test_answer

print(test_answer())
