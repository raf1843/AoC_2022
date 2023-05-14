#!/usr/bin/python3


with open('dirout.txt', 'r') as f:
    cmds = f.read().splitlines()

sizes = {}
dirs = {}
parent = "/"

for line in cmds:
    if "$ ls" in line:
        continue
    elif "dir" in line:
        dirname = line.split()[1]
        if parent not in dirs.keys():
            dirs.update({parent: []})
        dirs[parent].append(dirname)
    elif "$ cd" in line:
        cdto = line.split()[2]
        parent = cdto
    else:
        fsize, fname = line.split()[0], line.split()[1]
        if parent not in sizes.keys():
            sizes.update({parent: 0})  
        sizes[parent] += int(fsize)

total = 0
for d in dirs:
    if d not in sizes:
        continue
    elif sizes[d] <= 100000:
        total += sizes[d]
    for e in dirs[d]:
        if e not in dirs and e in sizes:
            total += sizes[e]
print(total)

