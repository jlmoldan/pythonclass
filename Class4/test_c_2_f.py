# test_c_to_f
# Jason Moldan

import pytest
import c_2_f


def test_freezing():
    assert c_2_f.c2f(0.0) == 32.0

def test_boiling():
    assert c_2_f.c2f(100) == 212

