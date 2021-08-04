import sys
import math
import functools
import re

def encode(binGroup):
    code = ""
    if binGroup[0:1] == "1":
        code += "0 "
        code += ''.join(["0" * len(binGroup)])
        code += " "
    else:
        code += "00 "
        code += ''.join(["0" * len(binGroup)])
        code += " "
    return code

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

chars = list(message) #split towards chars list
charsBin = list(map(lambda x : bin(ord(x))[2:], chars)) #convert to binary
charsBin7 = list(map(lambda x : x.zfill(7), charsBin)) #ensure 7 digit with leading 0s
sentenceBin = functools.reduce(lambda x,y : x + y, charsBin7) #join all chars to one sentence

binGroups= list(re.findall(r"1+|0+",sentenceBin)) #split in 1 or 0 groups

encryptionMap = list(map(encode, binGroups)) #encrypt each group

cnCode = (functools.reduce(lambda x,y : x + y, encryptionMap)).strip(" ") #join all encryted groups to a sentence"

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(cnCode)
