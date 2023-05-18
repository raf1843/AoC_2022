#!/usr/bin/python3

def check(cycle, x):
    # nth cycles to be checked
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        #print(cycle, '=', cycle*x) 
        # signal strength comes from cycle*x
        return cycle*x
    else:
        return 0

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
        strength += check(cycle, x)
    elif i[0] == 'addx':
        amt = int(i[1])
        # must check after each cycle
        cycle += 1
        strength += check(cycle, x)
        cycle += 1
        strength += check(cycle, x)
        # adding happens only after both cycles have passed
        x += amt
print(strength)
    
