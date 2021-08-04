import sys
import math
import string
 
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
 
l = int(input())
h = int(input())
t = input()
 
chars = list(t)
charsPos = list(map(lambda x :ord(x.lower()) - 96 - 1, chars))
CharsPosCleaned = list(map(lambda x : x if x >= 0 else 26  , charsPos))
print((t, chars, charsPos, CharsPosCleaned), file=sys.stderr, flush=True)
 
asciiArtLine = ""
 
for i in range(h):
    row = input()
    for j in range(len(CharsPosCleaned)):
        start = (CharsPosCleaned[j])*l
        end = (CharsPosCleaned[j])*l+l
        asciiArtLine += row[start:end]
    print(asciiArtLine, file=sys.stdout, flush=True)
    asciiArtLine = ""
 
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
 
