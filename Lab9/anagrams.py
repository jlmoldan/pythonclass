"""
Lab 9-2 Module: anagrams.py:

Find and print all words in the largest set of anagram-like words

Starting code...

You will find the following operations useful:

    charlist = list(string) => create a list of single chars in string
    word = "".join(charlist) => join charlist back into a word

"""

def makeSorted(w):
    '''
    Build new string with all w's chars in sorted order:
        finish this
    '''
    list_w = list(w)
    list_w.sort()
    result = ''.join(list_w)
    return result

wordFile = open("words.txt","r")

# Initialize anagrams as empty dict

anagrams = {}

count = 0
for word in wordFile:

    # Strip trailing newline

    word = word.strip()

    # Create alpha_sort: sorted chars in stripped word
    
    alpha_sort = makeSorted(word)
    
    # If alpha_sort already in anagrams dictionary as key:
    #   Append stripped word to anagrams[alpha_sort]
    #          (adding to list of all words having same chars)
    # else:
    #   Set anagrams[alpha_sort] to new list with only stripped word
    #          ([word])
    if alpha_sort in anagrams.keys():
        anagrams[alpha_sort].append(word)
    else:
        anagrams[alpha_sort] = [word]
#####print (anagrams)
wordFile.close()

# Here, anagrams has all "anagram lists" for dictionary:
# Now build tuple w/ first int elt as length of value list,
#   2nd as value list

anagram_freq = []
for v in anagrams.values():
    anagram_freq.append( (len(v),v) )

anagram_freq.sort(reverse=True)

# for each list value v in anagrams
#      append ((len(v),v)) to anagram_freq

# sort anagram_freq in reverse order, which orders by length of list v

# print first 20 values of anagram_freq

for elt in anagram_freq[:20]:
    print (elt)
