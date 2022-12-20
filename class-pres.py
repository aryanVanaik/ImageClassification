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

possObj = poss("11123")

print(possObj.replaceLowestValue())





