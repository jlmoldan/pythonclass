# gene.py
# Jason Moldan
#

stop_codon_list = ["TAA", "TAG", "TGA"]  # the rest stop codons
codon_list = ["ATG", "TAA", "TAG", "TGA"]

def is_valid_DNA(seq):
    valid = "ACGT"
    for eachChar in seq:
        if eachChar not in valid:
            return ("ERROR - Invalid Character Entered")
    return (is_gene(seq))  #passes first test now off to the next
    #is_gene(seq)

def is_gene(dna):
    # print (dna)
    if len(dna) %3 != 0:                    # second step length is a multiple of 3
        return ("ERROR - Not divisible by 3")
    # else:
    #     print(" divisible by 3")
   #print (dna[0:3])
    if (dna[:3]) != 'ATG':                  # begins with ATG   #ATG Start codon
        return ("ERROR - Does not beging with ATG")
    #print (dna[-3:])
    # print (stop_codon_list)
    if (dna[-3:]) not in stop_codon_list:          # ends with TAA/TAG/TGA
        return ("ERROR - Invalid Stop Codon")
    #print (dna[0:-3])
    #print (stop_codon_list)
    for codon in (stop_codon_list):   # THIS BLOCK WORKS - UGLY BUT OWKRS
        #print (codon)
        if codon in (dna[0:-3]):
            return ("ERROR - Stop Codon found between first and last codon")
        else:
            return ("Is potential gene")
    # if (dna[0:-3]) in stop_codon_list:                                                         ### FIGURE OUT HOW TO SLICE ALL BUT THE LAST 3 CHARACTERS. THEM WE WAND TO BE A VALID CODON
    #      return ("ERROR - Stop Codon found between first and last codon")



    #No TAG,TAA, TGA in (use in) inside the sequence before the last 3 characters.

print (is_valid_DNA(input("Enter a string:")))  # First Step - make sure they are valid characters.

#is_gene()
