#!/usr/bin/python3

# read in moves
moves = []
with open('moves.txt', 'r') as f:
    moves = f.read().splitlines()

head = [0,0]
tail = [0,0]
tailpos = []
tailcount = 0
for move in moves:
    move = move.split()
    for i in range(int(move[1])):
        # head moves
        # right
        if move[0] == 'R':
            head[0] += 1
        # left
        elif move[0] == 'L':
            head[0] -= 1
        # up
        elif move[0] == 'U':
            head[1] += 1
        # down
        elif move[0] == 'D':
            head[1] -= 1
        # tail moves
        # same column
        if head[0] == tail[0]:
            # needs to be a difference of at least two
            # sign determines whether to add or subtract from tail
            if head[1] - tail[1] >= 2:
                tail[1] += 1
            elif head[1] - tail[1] <= -2:
                tail[1] -= 1
        # same row
        elif head[1] == tail[1]:
            if head[0] - tail[0] >= 2:
                tail[0] += 1
            elif head[0] - tail[0] <= -2:
                tail[0] -= 1
        # tail is not diagonal-touching
        elif tail[0] not in range(head[0]-1, head[0]+2) or \
                tail[1] not in range(head[1]-1, head[1]+2):
            if head[0] > tail[0]:
                tail[0] += 1
            else:
                tail[0] -= 1
            if head[1] > tail[1]:
                tail[1] += 1
            else:
                tail[1] -= 1
        if tail not in tailpos:
            tailpos.append(tail.copy()) # have to do copy
            tailcount += 1
print(tailcount)
