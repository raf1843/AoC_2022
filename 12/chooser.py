#!/usr/bin/python3

# get all neighbors for a given position
def getNeighbors(pos):
    neighbs = []
    neighbs.append([pos[0]-1, pos[1]])
    neighbs.append([pos[0]+1, pos[1]])
    neighbs.append([pos[0], pos[1]-1])
    neighbs.append([pos[0], pos[1]+1])
    return neighbs

# return allowed neighbors for a given position
def allowed(pos, rows, cols):
    return pos[0] >= 0 and pos[0] < rows and pos[1] >= 0 and pos[1] < cols

# get empty steps matrix
def initSteps(rows, cols):
    steps = []
    for r in range(rows):
        steps.append([0]*cols)
    return steps

# parse puzzle
elevs = []
with open('puzzle.txt', 'r') as f:
    elevs = [[c for c in line] for line in f.read().splitlines()]
rows = len(elevs)
cols = len(elevs[0])

# all a elevations are possible starting points
starters = []
end = []
steps = []
# find start and end in the elevations matrix
# replace with letter representation
for e in elevs:
    idx = elevs.index(e)
    if 'S' in e:
        elevs[idx][elevs[idx].index('S')] = 'a'
    if 'a' in e:
        for c in range(len(e)):
            if e[c] == 'a':
                starters.append([idx, c])
    if 'E' in e:
        end = [idx, elevs[idx].index('E')]
        elevs[idx][elevs[idx].index('E')] = 'z'

# DEBUG: print(starters)

# DEBUG: for e in elevs: print(e)

# This would be one way to do it, but it's painfully slow
#results = []
#for start in starters: 
# Reddit came through for this puzzle
queue = []
visited = []
steps = initSteps(rows, cols)
# add starting position to queue
queue.append(end)
# loop until no more to search
while queue:    
    # get the next position off the queue
    pos = queue.pop(0)
    # once we get to the end, all done
    if pos in starters:
        #print("all done")
        print(steps[pos[0]][pos[1]])
        break
    # otherwise keep looking
    # no need to check something again that's already in visited
    elif pos in visited:
        continue
    # DEBUG: print("Position:", pos)
    # now we have visited the current position
    visited.append(pos)
    # go get the neighbors (up down left right)
    neighbors = getNeighbors(pos)
    for n in neighbors:
        # if a neighbor is in the starting list, that route would obviously be faster
        # allowed makes sure neighbor is within grid
        # rows, cols defined during initial parse
        # check that neighbor has not already been visited
        if allowed(n, rows, cols) and n not in visited:
            # DEBUG: print("Allowed:", n)
            # get elevation of the current neighbor
            el = ord(elevs[n[0]][n[1]])
            # DEBUG: print(ord(elevs[pos[0]][pos[1]]), str(el-1)+"-"+str(el+1))
            # can get to that destination as long as new elevation is at most 1 higher (any lower is okay)
            if ord(elevs[pos[0]][pos[1]]) - el <= 1:
                # DEBUG: print("In range:", n)
                # if reachable, give number of steps
                # (one more than current number)
                # and append to queue
                steps[n[0]][n[1]] = steps[pos[0]][pos[1]] + 1
                queue.append(n)
                # DEBUG: print("Queue", queue)

    # DEBUG: for s in steps: print(s)
    # This prints number of steps
    # print(steps[end[0]][end[1]])
    #other method: results.append(steps[end[0]][end[1]])
    #print(min(results))

