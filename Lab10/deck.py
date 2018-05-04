'''
Represents a standard deck of 52 playing cards,
requiring Card import
'''

#
# deck.py:
#
# 	Starting code for L10
#

import random
import card


class Deck():
    """
	Represents a deck of 52 standard playing cards,
		as a list of Card refs
	"""

    def __init__(self):
        '''
		Initialize deck: field _cards is list containing
			52 Card refs, initially
		'''

        self._cards = []
        for rank in range(1, 14):
            for suit in range(4):
                c = card.Card(rank, suit)
                self._cards.append(c)

    def __str__(self):
        '''
		"Stringified" deck: string of each Card,
		concatenated with '\n' for easier reading
		'''
        toreturn = ''

        # for index in range(len(self._cards)):
        #     self._cards[index]

        for c in self._cards:
            temp = str(c)  # temp is the stringified card
            toreturn = toreturn + temp + "\n"  # note \n at end

        return toreturn

    def shuffle(self):
        random.shuffle(self._cards)  # note random function to do this

    def dealCard(self):
        toreturn = self._cards.pop(0)  # get and remove top card from deck
        return toreturn




## L10-1: add new method randomCard()
    def randomCard(self):
        rank = random.randint(1, 13)  # randint goes through second argument (include both endponts) rand range does not
        suit = random.randint(0, 4)
        c = card.Card(rank, suit)
        return c
## L10-3: add new method dealHand()
    def dealHand(self):
        hand = []
        for count in range(5):
            try:
                c = self.dealCard()
            except IndexError:
                self.__init__()
                c = self.dealCard()
            hand.append(c)

        return hand

    def outRiffle(self): ########################## don't know if it works.......
        top_half = []
        bottom_half = []

        # deal half of deck into top half
        for count in range(len(self._cards)//2):  ### NOT SURE WHAT MESSED UP HERE>... But broke it.....  Middle/end of video 2.
        #for count in range(len(self._cards // 2)):
            c = self.dealCard()
            top_half.append(c)
        # deal reamining in self to bottom half
        for c in self._cards: #### added _ on this -- correct?
            bottom_half.append(c)
        #clear out curent deck
        self._cards=[]

        for c in top_half:
            self._cards.append(c)
            bc = bottom_half.pop(0)
            self._cards.append(bc)

        for c in bottom_half:
            self._cards.append(c)



## L10-4: add new method outRiffle()


def main():
    '''
	Create, print then shuffle, print again
	Then deal first two cards and print, along with bottom card
	'''

    # create and print new Deck

    deck = Deck()
    print(str(deck))

    # shuffle and print Deck

    print("Now we shuffle:\n")

    deck.shuffle()
    print(str(deck))

    # deal two cards from Deck, and report them

    c = deck.dealCard()
    c2 = deck.dealCard()

    print("The first card dealt is", str(c), "and the second is", str(c2))
    print("Bottom of deck is", deck._cards[-1])  # can't hide the implementation!


if __name__ == "__main__":
    main()
