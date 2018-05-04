#
# two_aces.py:
#
# 	Starting code for L10-2
#

import deck

TRIALS = 10000

def main():
    # count how many times this occurs:
    #   create Deck, shuffle, draw top two cards and both are aces
    twoAces = 0
    for count in range(TRIALS):
        d = deck.Deck()
        d.shuffle()

        card1 = d.dealCard()
        card2 = d.dealCard()

        if card1._rank == 1 and card2._rank == 1:
            twoAces += 1
    print("Percentage is %.4f" % (100.0 * twoAces / TRIALS))

    # print percentage of time this occurs

    pass

main()