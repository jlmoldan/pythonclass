




import string
FILENAME = 'alice.txt'

fvar = open (FILENAME, 'r')

allwords = []

for aline in fvar:
	line = aline.lower()
	





	words = line.split()



	allwords.extend(words)




allwords.sort()

print (string.punctuation)


print (len(allwords))
fvar.close()


