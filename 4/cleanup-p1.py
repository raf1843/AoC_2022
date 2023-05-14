#!/bin/python

assignments = []
count = 0
with open('pairs.txt', 'r') as f:
    assignments = f.readlines()
for assignment in assignments:
    pairs = assignment.strip().split(',')
    pairs[0] = pairs[0].split('-')
    pairs[1] = pairs[1].split('-')
    if (int(pairs[0][0]) >= int(pairs[1][0]) \
      and int(pairs[0][1]) <= int(pairs[1][1])) \
    or (int(pairs[0][0]) <= int(pairs[1][0]) \
      and int(pairs[0][1]) >= int(pairs[1][1])):
           count += 1
print(count)
