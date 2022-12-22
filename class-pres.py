from itertools import *

from poss import poss


perms = [''.join(p) for p in permutations('01234')]
combos = combinations_with_replacement('01234',5)

def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str

comboArr = []
for i in combos:
    comboArr.append(convertTuple(i))



# How to use the program 

# comboArr contains all possible string with length 5 and number 01234 with replacement
# You can use this to filter a string based on a condition

# For a single string the program works like this 
# 1. Create a variable that implements the class poss like this 
possObj = poss("01234")
# 2. To use any of the methods and print them on the terminal from thr class poss do this 
# here we call the print function that prints to the console
# inside the print type the name of the variable you have used to create the object 
# with a "." and type the name of the function all functions are contained in poss class
print(possObj.countOccurance())








