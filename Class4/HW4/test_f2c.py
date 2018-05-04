# test_c_to_f
# Jason Moldan

import pytest
import f_2_c

def test_freezing():
    assert f_2_c.f2c(32.0) == 0

def test_boiling():
    assert f_2_c.f2c(176) == 80

def test_randomA():
    assert f_2_c.f2c(-40) == -40

def test_randomB():
    assert f_2_c.f2c(212) == 100

def test_randomC():
    #assert f_2_c.f2c(20.0) == -6.66667
    assert round(f_2_c.f2c(20.0),5) == -6.66667

def test_randomD():
    assert f_2_c.f2c(14) == -10


def test_randomE():
    assert f_2_c.f2c(-148) == -100


def test_randomF():
    assert f_2_c.f2c(190.4) == 88


def test_randomG():
    assert f_2_c.f2c(77) == 25


def test_randomH():
    assert f_2_c.f2c(212) == 100