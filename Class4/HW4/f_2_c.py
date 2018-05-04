# f2c.py
# Jason Moldan

# c_to_f.py
# Jason Moldan

###  T(°F) = T(°C) × 1.8 + 32
#### temp F - 32 * 5/9

#fTemp= float(input("Enter the temp in Farenheit: "))
def f2c(fTemp):
    cTemp = (fTemp - 32) * (5/9)
    return cTemp

#print (fTemp, "Farenheit is", f2c(fTemp), "in Celcius")
