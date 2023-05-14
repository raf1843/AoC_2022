#!/bin/python3

with open("rucksack.txt", "r") as file:
	sacks = file.readlines()

likes = []
priorities = 0
for sack in sacks:
    first = sack[:len(sack)//2]
    second = sack[len(sack)//2:]
    for c in first:
        if c in second:
            likes.append(c)
            break
for c in likes:
    if c.islower():
        priorities += (ord(c) - 96)
    else:
        priorities += (ord(c) - 38)
print(priorities)
