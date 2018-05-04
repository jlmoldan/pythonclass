# test_num2eng.py
# Jason Moldan
import pytest
import num2eng4_t



def test_101():
    assert num2eng4_t.checkValid(101) == "invalid"
def test_55():
    assert num2eng4_t.checkValid(55) == "Fifty Five"
def test_22():
    assert num2eng4_t.checkValid(22) == "Twenty Two"
def test_33():
    assert num2eng4_t.checkValid(33) == "Thirty Three"
def test_11():
    assert num2eng4_t.checkValid(11) == "Eleven"
def test_2():
    assert num2eng4_t.checkValid(2) == "Two"
def test_3():
    assert num2eng4_t.checkValid(3) == "Three"
def test_59():
    assert num2eng4_t.checkValid(59) == "Fifty Nine"
def test_0():
    assert num2eng4_t.checkValid(0) == "invalid"
def test_333():
    assert num2eng4_t.checkValid(333) == "invalid"
def test_n2():
    assert num2eng4_t.checkValid(-2) == "invalid"
def test_27():
    assert num2eng4_t.checkValid(27) == "Twenty Seven"
def test_99():
    assert num2eng4_t.checkValid(99) == "Ninety Nine"
def test_555():
    assert num2eng4_t.checkValid(555) == "invalid"
def test_20():
    assert num2eng4_t.checkValid(20) == "Twenty"
def test_30():
    assert num2eng4_t.checkValid(30) == "Thirty"
def test_50():
    assert num2eng4_t.checkValid(50) == "Fifty"
def test_82():
    assert num2eng4_t.checkValid(82) == "Eighty Two"
def test_43():
    assert num2eng4_t.checkValid(43) == "Fourty Three"
def test_66():
    assert num2eng4_t.checkValid(66) == "Sixty Six"

