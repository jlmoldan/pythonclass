"""
Lab 9-1 Module: count_letters.py:

Print out frequency counts of all letters 'a'..'z', 'A'..'Z' found in input string.
Only counts >0 should be printed

Starting code follows...

"""

st = input ("Enter a string to count: ")

print ("You entered '%s'" % st)

# for index in range(len(st)):
#    st[index] ..

#  initialize dictionary counts to empty

counts = {}



for ch in st:
    #   add 1 to counts[ch] if there,
    #   initialize counts[ch] to 1 if not
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':   # ensure only ascii via # if ch in string.ascii_letters or
        if ch in counts.keys():
            counts[ch] = counts[ch] + 1
        else:
            counts[ch] = 1

# sort keys
sorted_keys = list(counts.keys())
sorted_keys.sort()

#print (sorted_keys)
#print (counts)

# iterate through sorted keys, printing in this format:
#   'E' - 47

for key in sorted_keys:
    print("'%s' - %d" % (key, counts[key]))

# Example line of output for key k, value v==counts[k]
# print ("'%s' - %d" % (k,v))
    

    
