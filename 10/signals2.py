#!/usr/bin/python3

def check(cycle, x):
    # CRT prints mid-cycle, hence cycle-1
    # rows are 40 chars long
    # x-1, x, and x+1 all valid positions
    if (cycle-1) % 40 in range(x-1, x+2):
        print('#', end='')
    else:
        print('.', end='')
    if cycle % 40 == 0:
        print()

# read in instructions
instructions = []
with open('instructions.txt', 'r') as file:
    instructions = file.read().splitlines()

# value in x starts at 1, cycle starts at 0
x = 1
cycle = 0
strength = 0
# analyze each instruction
# noop = 1 cycle, addx = 2 cycles
for i in instructions:
    amt = 0
    i = i.split()
    if i[0] == 'noop':
        cycle += 1
        check(cycle, x)
    elif i[0] == 'addx':
        amt = int(i[1])
        # must check after each cycle
        cycle += 1
        check(cycle, x)
        cycle += 1
        check(cycle, x)
        # adding happens only after both cycles have passed
        x += amt
    
