# inverse.py
# Jason Moldan

def km_to_miles(km):
    miles = km * 0.62137
    return miles

def miles_to_km(miles):
    km = miles / 0.62137
    return km

#print ("miles is",km_to_miles(10))
#print ("KM is", miles_to_km(6.2))
#print (miles_to_km(km_to_miles(10)))

import pytest
import inverse


def test_km():
    assert (miles_to_km(km_to_miles(10))) == 10

def test_km2():
    assert (miles_to_km(km_to_miles(1.5))) == 1.5

def test_km3():
    assert round((miles_to_km(km_to_miles(27))),0) == 27