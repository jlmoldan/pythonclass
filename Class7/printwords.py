#
#   printwords.py:
#
#       Starting code for Lab 7-3
#

FILENAME = 'words.txt'

fvar = open (FILENAME, 'r') # open file for reading

allwords = []        # b accumulator
maxLenSoFar = 0      # c accumulator
maxLenString=[]
maxLenStrings = []   # c accumulator
first2last2Count = 0 # d accumulator
numEndingWithE = 0   # e
maxLenCount = 0
#bigline = fvar.read()

for aline in fvar:
    #print (aline.rstrip()) #  a  ### rstrip removes empty space
    # print (aline[:-1])  #a strip last character instead....
    next_word = aline.rstrip()
    #print (next_word)
    if len(next_word) > maxLenSoFar:
        maxLenString = next_word  # Longest word
        maxLenSoFar = len(maxLenString)
        #print (maxLenSoFar)
        maxLenCount = (maxLenCount)+1
    if next_word[:2] == next_word[-2:] and len(next_word) > 2:   #d
         pass
         #print (next_word)
         first2last2Count = first2last2Count +1
    if next_word[:-1] == 'e':
        numEndingWithE = numEndingWithE + 1

    # number_of_e = bigline.count('e')
    # print("Frequency of 'e' is %d" % (number_of_e))
    allwords.append(aline.rstrip())  # b puts all words into a list
#print (len(allwords))  #added just to count all words


print ("Maximum length is %d" % maxLenSoFar) # c
print ("Maximim length string is %s" % maxLenString)   #c - longest word
print ("Strings with this length:",maxLenCount) # c   #####NOT DONE
print ("Number of words with first 2 == last 2:",first2last2Count) # d
print ("Number of words ending in 'e':", numEndingWithE) # e
print ("List of all words:",allwords) # b



fvar.close()
