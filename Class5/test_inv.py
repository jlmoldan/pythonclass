import pytest
import inverse


def test_km():
    assert (inverse.miles_to_km(inverse.km_to_miles(10))) == 10

def test_km2():
    assert (inverse.miles_to_km(inverse.km_to_miles(1.5))) == 1.5