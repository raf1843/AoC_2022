#!/usr/bin/python3

cmds = []
with open('dirout.txt', 'r') as f:
    cmds = f.read().splitlines()

path = ""
dirs = {}
dirs.update({'/': 0})
for line in cmds:
    line = line.split()
    # if user input
    if line[0] == '$':
        if line[1] == 'ls':
            continue
        # change directory
        elif line[1] == 'cd':
            # remove a directory from path (go up)
            if line[2] == '..':
                path = path[:path.rindex('/')]
                # cannot go back any further than root
                if path == "":
                    path = '/'
            # go to root
            elif line[2] == '/':
                path = '/'
            # add directory to path   
            else:
                if path == '/':
                    path = path + line[2]
                else:
                    path = path + '/' + line[2]
                dirs.update({path: 0})
    # not user input
    else:
        # add file sizes to every directory in path
        if line[0] != "dir":
            fsize = int(line[0])
            temppath = path
            # avoid double counting root
            if temppath != '/':
                while temppath != "":
                    dirs[temppath] += fsize
                    temppath = temppath[:temppath.rindex('/')]
            dirs['/'] += fsize
# sum up using conditional
rm = ""
for d in dirs:
    if 70000000 - dirs['/'] + dirs[d] >= 30000000:
        if rm == "" or dirs[d] <= dirs[rm]:
            rm = d
print(rm, dirs[rm])
#print(dirs)
