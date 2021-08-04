import sys
import math
 
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
 
def max(a, b):
    if a >= b:
        return a
    else:
        return b
 
cur = math.inf
output = 0
 
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    abst = abs(int(i))
    abscur = abs(cur)
    if abst == abscur:
        cur = max(t,cur)
    elif abst < abscur:
        cur = t
    print((t,cur), file=sys.stderr, flush=True)
    output = cur
 
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
 
print(output)
 
