#!/usr/bin/python3

lines = []
with open('map.txt', 'r') as f:
    lines = f.read().splitlines()

totals = []
scenic = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        uscore, dscore, lscore, rscore = 0, 0, 0, 0
        # edges always visible
        if i == 0 or j == 0 or i == len(lines)-1 or j == len(lines[i])-1:
            continue
        # look up
        for k in range(i-1, -1, -1):
            #print("up:",lines[k][j])
            uscore += 1
            if lines[k][j] >= lines[i][j]:
                break
        # look down
        for k in range(i+1, len(lines)):
            dscore += 1
            #print("down:",lines[k][j])
            if lines[k][j] >= lines[i][j]:
                break
        # look left
        for l in range(j-1, -1, -1):
            lscore += 1
            #print("left:",lines[i][l])
            if lines[i][l] >= lines[i][j]:
                break
        # look right
        for l in range(j+1, len(lines[i])):
            rscore += 1
            #print("right:",lines[i][l])
            if lines[i][l] >= lines[i][j]:
                break
        #print(uscore, dscore, lscore, rscore)
        scenic = uscore * dscore * lscore * rscore
        #print(scenic)
        totals.append(scenic)

print(max(totals))
