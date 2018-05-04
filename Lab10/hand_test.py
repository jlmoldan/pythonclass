#
# hand_test.py:
#
# 	Starting code for L10-3
#
#   Also requests dealHand() method added to Deck
#
#########See video 2......

import deck as d


def main():
    deck1 = d.Deck()
    deck1.shuffle()

    for count in range(11):
        hand = deck1.dealHand()
        for c in hand:
            print(c, end=' -- ')
        print()

    # Repeat the following 11 times:
    #   deal 5 card hand using Deck dealHand()

    # What happens? Fix by handling exceptions in dealHand()


main()
