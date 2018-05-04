#
#   onestring.py:
#
#     Starting code for Lab 7-2
#

FILENAME = 'words.txt'
fvar = open (FILENAME, 'r') # open file for reading
bigline = fvar.read()
#print (bigline)

# L7-2a: print out # of characters in line. Notice the % formatting...

print ("Number of characters is: %d" % len(bigline))  #%d = decimal integer.....

# L7-2b: print out # of words in file (one word per line).
print ("Numeber of words is: %d" % bigline.count('\n'))  # number of words

# L7-2c: print out avg length of word (# non-newline chars/# words)
# Average word length
total_chars = len(bigline)
num_words = bigline.count('\n')
total_alpha_chars = total_chars - num_words # gets rid of new lines which count as characters
avg_word_length = total_alpha_chars / num_words
print ("Average word length is %.2f" % avg_word_length)

# L7-2d: print 'e' count, along with fractional frequency of 'e' among all letters
total_alpha_chars = total_chars - num_words
number_of_e = bigline.count('e')
print ("Frequency of 'e' is %.4f" % (number_of_e/total_alpha_chars))


# total_alpha_chars = total_chars - num_words
# number_of_z = bigline.count('z')
# print ("Frequency of 'z' is %.4f" % (number_of_z/total_alpha_chars))


fvar.close()


