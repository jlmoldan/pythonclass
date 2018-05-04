#
# out_riffle.py:
#
# 	Starting code for L10-4
#
#   Add outRiffle() to Deck, implementing out-riffle shuffle

#   Then use it to demonstrate how many out-riffle-shuffles it
#       takes to return a deck to its original order

import card as c
import deck as d

def main():
    # create new Deck, shuffle it
    # keep track of how many out-riffles have been performed so far
    deck1 = d.Deck()
    orig_order = str(deck1)

    numOutRiffles = 0
    while True:
        deck1.outRiffle()
        numOutRiffles += 1

        if str(deck1) == orig_order:
            print ("done in %d " % numOutRiffles)
            break

        # do an out-riffle
        # check if resulting deck is same as original:
        #   if so, print out message and break loop

main()