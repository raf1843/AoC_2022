#!/usr/bin/python3
import re

stacks = []
todo = []
with open("input.txt", 'r') as f:
    line = f.readline().rstrip()
    while line != "":
        for i in range(0,36,4):
            sub = line[i+1:i+2]
            try:
                stacks[i//4].append(sub)
            except IndexError:
                stacks.append([])
                stacks[i//4].append(sub)
        line = f.readline().rstrip()
    for s in stacks:
        num = s.pop()
        s.reverse()
        while s[-1] == ' ':
            num = s.pop()
    line = f.readline().rstrip()
    while line != "":
        inst = re.findall(r'\d+', line)
        todo.append(inst)
        line = f.readline().rstrip()

for inst in todo:
    num = int(inst[0])
    src = int(inst[1]) - 1
    dst = int(inst[2]) - 1
    for i in range(num):
        stacks[dst].append(stacks[src].pop())

for s in stacks:
    print(s)
