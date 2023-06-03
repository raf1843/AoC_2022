#!/usr/bin/python3

def getNeighbors(pos):
    neighbs = []
    neighbs.append([pos[0]-1, pos[1]])
    neighbs.append([pos[0]+1, pos[1]])
    neighbs.append([pos[0], pos[1]-1])
    neighbs.append([pos[0], pos[1]+1])
    return neighbs

def allowed(pos, rows, cols):
    return pos[0] >= 0 and pos[0] < rows and pos[1] >= 0 and pos[1] < cols



elevs = []
with open('puzzle.txt', 'r') as f:
    elevs = [[c for c in line] for line in f.read().splitlines()]
rows = len(elevs)
cols = len(elevs[0])

start = []
end = []
steps = []
# find start and end in the elevations matrix
# replace with letter representation
for e in elevs:
    idx = elevs.index(e)
    if 'S' in e:
        start = [idx, elevs[idx].index('S')]
        elevs[idx][elevs[idx].index('S')] = 'a'
    if 'E' in e:
        end = [idx, elevs[idx].index('E')]
        elevs[idx][elevs[idx].index('E')] = 'z'
    steps.append([0]*len(e))


# DEBUG: for e in elevs: print(e)

# got real stumped on this so trying traditional BFS
# + following guides (credit: Captain Coder on YT)
# Note: I think my problem the whole time was not considering that the dest could be more than one lower. oops.
queue = []
visited = []

# add starting position to queue
queue.append(start)
# loop until no more to search
while queue:    
    # get the next position off the queue
    pos = queue.pop(0)
    # once we get to the end, all done
    if pos == end:
        print("all done")
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
        # allowed makes sure neighbor is within grid
        # rows, cols defined during initial parse
        # check that neighbor has not already been visited
        if allowed(n, rows, cols) and n not in visited:
            # DEBUG: print("Allowed:", n)
            # get elevation of the current neighbor
            el = ord(elevs[n[0]][n[1]])
            # DEBUG: print(ord(elevs[pos[0]][pos[1]]), str(el-1)+"-"+str(el+1))
            # can get to that destination as long as new elevation is at most 1 higher (any lower is okay)
            if el - ord(elevs[pos[0]][pos[1]]) <= 1:
                # DEBUG: print("In range:", n)
                # if reachable, give number of steps
                # (one more than current number)
                # and append to queue
                steps[n[0]][n[1]] = steps[pos[0]][pos[1]] + 1
                queue.append(n)
                # DEBUG: print("Queue", queue)

# DEBUG: for s in steps: print(s)
# This prints number of steps
print(steps[end[0]][end[1]])

