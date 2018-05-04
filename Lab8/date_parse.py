#
# starting code for L8-2
#

def parse_date(dstring):
    result = dstring.split('/')
    #return tuple(result)  # this works.... but also so does..
    return int(result[0]), int(result[1]), int(result[2])




def main():

    date = input ("Enter date in form mm/dd/yyyy: ")
    result = parse_date(date)
    print (result)

main()