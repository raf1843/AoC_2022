#!/bin/python3

with open("rucksack.txt", "r") as file:
	sacks = file.readlines()

badges = []
priorities = 0
for idx in range(0,len(sacks),3):
    print(idx)
    sack1 = sacks[idx]
    sack2 = sacks[idx+1]
    sack3 = sacks[idx+2]
    for c in sack1:
        if c in sack2 and c in sack3:
            badges.append(c)
            break
for c in badges:
    if c.islower():
        priorities += (ord(c) - 96)
    else:
        priorities += (ord(c) - 38)
print(priorities)
