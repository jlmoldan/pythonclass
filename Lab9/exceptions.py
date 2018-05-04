# Define a function read_float_gt0() which prompts the user to enter a float value greater than 0.0, then returns it.
# However, if the user enters an illegal float value, "floatifying" the entered string will throw a TypeError.
# If the user enters a valid float, but it's <= 0.0, then throw your own ValueError.



def read_float_gt0():
    float_str = input ("Enter a float > 0.0: ")
    to_return = float(float_str)

    if to_return <= 0.0:
        raise TypeError # may raise a value error
    return to_return
def main():

    while True:
        try:
            print (read_float_gt0())
            break
        except ValueError:
            print ("bad float entered. Retry. ")
        except TypeError:
            print ("float less than <= 0.0 entered.  Retry. ")
main()
