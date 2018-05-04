#
# tab_expand.py:
#
#   Starting code Lab 8-3
#

fname = input ("Enter file name: ")

fvar = open(fname, 'r')

outfvar = open('tab_'+fname, 'w')

for aline in fvar:
    #print (aline, end'')
    newline = aline.replace('\t', 'tab')
    outfvar.write(newline)
    #print (newline,end='')

outfvar.close()
fvar.close()
