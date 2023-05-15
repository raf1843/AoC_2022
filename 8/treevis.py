#!/usr/bin/python3

lines = []
with open('map.txt', 'r') as f:
    lines = f.read().splitlines()

vis = 0
flag = False
for i in range(len(lines)):
    for j in range(len(lines[i])):
        # edges always visible
        if i == 0 or j == 0 or i == len(lines)-1 or j == len(lines[i])-1:
            vis += 1
            continue
        # look up
        for k in range(i):
            if lines[k][j] < lines[i][j]:
                flag = True
            else:
                flag = False
                break
        if flag:
            vis += 1 
            continue
        # look down
        for k in range(i+1, len(lines)):
            if lines[k][j] < lines[i][j]:
                flag = True
            else:
                flag = False
                break
        if flag:
            vis += 1
            continue
        # look left
        for l in range(j):
            if lines[i][l] < lines[i][j]:
                flag = True
            else:
                flag = False
                break
        if flag:
            vis += 1
            continue
        # look right
        for l in range(j+1, len(lines[i])):
            if lines[i][l] < lines[i][j]:
                flag = True
            else:
                flag = False
                break
        if flag:
            vis += 1
            continue
print(vis)
