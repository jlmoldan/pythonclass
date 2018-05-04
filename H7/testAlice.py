#
# count_alice.py:
#
#   Starting code Lab 8-4
#
import string
FILENAME = 'alice.txt'

fvar = open (FILENAME, 'r') # open file for reading

allwords = [] # accumulate the words in this list

for aline in fvar:
	line = aline.lower()
	#line = line.replace('""', '').replace('--','').replace('?','').replace(',','')   #Stopped at 1:56 on the video at https://vimeo.com/260877405/ef0056381d

   # line = line.replace('string.punctuation', '')
   #  for ch in string.punctuation:
   #      line=line.replace(ch,'')

	words = line.split() # splits the line on whitespace (blanks, '\n', '\t'), and lowers the case of everything

    # remove punctuation
    # make lowercase
	allwords.extend(words) # this does...




allwords.sort()
#print (allwords[:1000])
print (string.punctuation)
# for word in allwords:
#     print(word)
print (len(allwords))
fvar.close()


