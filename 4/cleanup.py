#!/bin/python

assignments = []
count = 0
with open('pairs.txt', 'r') as f:
    assignments = f.readlines()
for assignment in assignments:
    pairs = assignment.strip().split(',')
    pairs[0] = pairs[0].split('-')
    pairs[1] = pairs[1].split('-')
    start1, end1 = int(pairs[0][0]), int(pairs[0][1])
    start2, end2 = int(pairs[1][0]), int(pairs[1][1])
    if start1 >= start2 and start1 <= end2:
        count += 1
    elif start1 <= start2 and end1 >= start2:
        count += 1
print(count)
