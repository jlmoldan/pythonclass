#
# count_alice2.py:
#
#   Starting code H7-1
#

# start with your Lab 7 count_alice and continue...


import string
FILENAME = 'alice.txt'

fvar = open (FILENAME, 'r') # open file for reading

allwords = [] # accumulate the words in this list

# for ch in string.punctuation:
#     line = line.replace(ch, '')
#
# words = line.split()


for aline in fvar:
    line = aline.lower()
    punct ='!"#$%&()*+,-/:;<=>?@[\]^_{|}~'
    for p in punct:
        line = line.replace(p,'')
    line = line.replace('--','')
    words = line.split()

    allwords.extend(words)



# for aline in fvar:
#     line = aline.lower()
#     special = "-"
#     if special not in aline:
#         words = line.split()
#     allwords.extend(words)


trimmed_allwords =[]
#################################################################
# for ind in range(len(allwords)):   #This does work..
#     if allwords[ind][0]=="'":
#         trimmed_word=allwords[ind][1:]
#         if trimmed_word is not '':
#             trimmed_allwords.append(trimmed_word)
#     else:
#         trimmed_allwords.append(allwords[ind])

    # for ch in string.punctuation:
    #     line=line.replace(ch,'')
##################################################################
for word in allwords:
    if word[0] =="'":
        if len(word) > 1:
            if word is not "'tis":
                trimmed_allwords.append(word[1:])
        else:
            trimmed_allwords.append(word)


     # splits the line on whitespace (blanks, '\n', '\t'), and lowers the case of everything
     # this does...

#print (allwords[:1000])
#print (string.punctuation)

trimmed_allwords.sort()
for word in trimmed_allwords:
    print (word)
# allwords.sort()
# for word in allwords:
#     print(word)
print (len(allwords))
fvar.close()