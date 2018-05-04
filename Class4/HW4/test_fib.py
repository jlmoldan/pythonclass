# test_fib
# Jason Moldan

import pytest
import fib


def test_1():
    assert fib.fib(1) == 1

def test_2():
    assert fib.fib(2) == 1

def test_3():
    assert fib.fib(3) == 2

def test_4():
    assert fib.fib(4) == 3

def test_5():
    assert fib.fib(5) == 5

def test_6():
    assert fib.fib(6) == 8

def test_7():
    assert fib.fib(7) == 13

def test_8():
    assert fib.fib(8) == 21

def test_9():
    assert fib.fib(9) ==34

def test_10():
    assert fib.fib(10) == 55

def test_11():
    assert fib.fib(0) == 0