#!/usr/bin/python3

# read in moves
moves = []
with open('moves.txt', 'r') as f:
    moves = f.read().splitlines()

knots = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
tailpos = []
tailcount = 0
for move in moves:
    move = move.split()
    for i in range(int(move[1])):
        # head moves
        # right
        if move[0] == 'R':
            knots[0][0] += 1
        # left
        elif move[0] == 'L':
            knots[0][0] -= 1
        # up
        elif move[0] == 'U':
            knots[0][1] += 1
        # down
        elif move[0] == 'D':
            knots[0][1] -= 1
        # rope moves
        for j in range(1,len(knots)):
            # same column
            if knots[j-1][0] == knots[j][0]:
                # needs to be a difference of at least two
                # sign determines whether to add or subtract from tail
                if knots[j-1][1] - knots[j][1] >= 2:
                    knots[j][1] += 1
                elif knots[j-1][1] - knots[j][1] <= -2:
                    knots[j][1] -= 1
            # same row
            elif knots[j-1][1] == knots[j][1]:
                if knots[j-1][0] - knots[j][0] >= 2:
                    knots[j][0] += 1
                elif knots[j-1][0] - knots[j][0] <= -2:
                    knots[j][0] -= 1
            # tail is not diagonal-touching
            elif knots[j][0] not in range(knots[j-1][0]-1, knots[j-1][0]+2) or \
                    knots[j][1] not in range(knots[j-1][1]-1, knots[j-1][1]+2):
                if knots[j-1][0] > knots[j][0]:
                    knots[j][0] += 1
                else:
                    knots[j][0] -= 1
                if knots[j-1][1] > knots[j][1]:
                    knots[j][1] += 1
                else:
                    knots[j][1] -= 1
            if knots[9] not in tailpos:
                tailpos.append(knots[9].copy()) # have to do copy
                tailcount += 1
print(tailcount)
