'''
test_pokerodds.py:

py.test unit test to check for one pair
'''
import pokerodds as p

def test_one_pair():

	testhand = [p.Card(2, 3), p.Card(1, 2), \
				p.Card(3, 1), p.Card(13, 2), \
				p.Card(2, 0)]

	dict = p.buildDict(testhand)

	assert p.hasOnePair(dict)