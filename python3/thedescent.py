import sys
import math
import functools

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

# game loop
while True:
    chain_h = []
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        chain_h.append(mountain_h)
    max_h = max(chain_h)
    max_index = chain_h.index(max_h)
    print((chain_h, max_h, max_index), file=sys.stderr, flush=True)
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # The index of the mountain to fire on.
    print(max_index)
