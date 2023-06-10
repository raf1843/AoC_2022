#!/usr/bin/python3.11

import sys

if len(sys.argv) != 2:
    print("Usage: regolith.py <puzzle-file>.txt")
    exit()

lines = []
with open(sys.argv[1], 'r') as f:
    lines = f.read().strip().splitlines()

points = []
for line in lines:
    line = line.split('->')
    tmp = []
    for l in line:
        tmp.append(list(eval(l.strip())))
    points.append(tmp)
# DEBUG: print(points)

paths = []
y = []
for point in points:
    for i in range(len(point)-1):
        start = point[i]
        end = point[i+1]
        temp = []
        if start not in paths:
            paths.append(start)
        if start[0] == end[0]:
            while start[1] < end[1]:
                temp = [start[0], start[1]+1]
                paths.append(temp)
                start = temp
            while start[1] > end[1]:
                temp = [start[0], start[1]-1]
                paths.append(temp)
                start = temp
        elif start[1] == end[1]:
            while start[0] < end[0]:
                temp = [start[0]+1, start[1]]
                paths.append(temp)
                start = temp
            while start[0] > end[0]:
                temp = [start[0]-1, start[1]]
                paths.append(temp)
                start = temp
        if temp[1] not in y:
            y.append(temp[1])
# DEBUG: print(paths)

bottom = max(y)

sand = (500,0)
pile = []

move = [500, 0]
possible = True
while possible:
    move = [500, 0]
    possible = False
    while move[1] <= bottom:
        moved = False
        if [move[0], move[1]+1] not in paths and [move[0], move[1]+1] not in pile:
            move[1] += 1
            moved = True
        elif [move[0]-1, move[1]+1] not in paths and [move[0]-1, move[1]+1] not in pile:
            move[0] -= 1
            move[1] += 1
            moved = True
        elif [move[0]+1, move[1]+1] not in paths and [move[0]+1, move[1]+1] not in pile:
            move[0] += 1
            move[1] += 1
            moved = True
        if not moved:
            # DEBUG: print(move)
            possible = True
            pile.append(move)
            break
print(len(pile))
