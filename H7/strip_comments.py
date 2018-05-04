#
# strip_comments.py:
#
#   Starting code H7-4
#

fname = input ("Enter file name: ")
fvar = open(fname, 'r')
outfvar = open('strip__'+fname, 'w')

#############THIS IS WORKING #########
# for line in fvar:
#     line=line.split("#")[0].strip() + '\n'
#     outfvar.write (line)
############## ABOVE WORKING ########
for line in fvar:
    newline=line.replace('\t', 'tab') #Newline and the strip kills tabbing, dirty way to put placeholder in and then remove it
    line=newline.split("#")[0].strip() + '\n'
    newline=line.replace('tab', '\t')
    outfvar.write (newline)

outfvar.close()
fvar.close()

