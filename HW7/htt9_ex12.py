# htt9_ex12.py
# Jason Moldan


#Write a function that removes all occurrences of a string from another string.


def main():
    s = input("Enter a string?")      # get user input
    sub = input("Enter a substring to be removed?")
    print (remove_all(sub, s))

def remove_all(substr, the_str):
    new_string = the_str.replace(substr, "")
    return new_string

main()
