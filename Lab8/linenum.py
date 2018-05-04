#
# linenum.py:
#
#   Starting code Lab 8-1
#

# read filename fname from user

# open file named fname for reading

# open file named 'lnum_' + fname for writing

# iterate over fname, line by line:

# add 'dddd: ' to start of line and write it out

# close both files

fname = input ("Enter file name: ")

fvar = open(fname, 'r')

outfvar = open('linenum_'+fname, 'w')
count = 1
for line in fvar:
#    counter=str("000")+str(count)

    outfvar.write (str(count).rjust(4,'0')+': ' +line)
    ##outfvar.write (str(count).zfill(4) +line)
    count= count+1
outfvar.close()
fvar.close()

