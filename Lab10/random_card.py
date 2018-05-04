#
# random_card.py:
#
# 	Starting code for L10-1
#
#   Modifies code in deck.py, then tests it below
#
import deck as d
TRIALS = 10000

def main():

    # Count number of times this occurs (loop TRIALS times):
    #   Deck.randomCard() generates two aces in a row
    deck1 = d.Deck()
    numTwoAces = 0

    for count in range(TRIALS):
        card1 = deck1.randomCard()
        card2 = deck1.randomCard()

        if card1._rank ==1 and card2._rank ==1:
           numTwoAces += 1
    print ("Percentage is %.4f" % (100.0 * numTwoAces / TRIALS))

    # Print percentage of time this occurs



main()