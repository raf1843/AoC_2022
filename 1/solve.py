#!/bin/python3

with open("rations.txt", "r") as file:
	elves = file.readlines()
	sum = 0
	rations = []
	# go through list, elves sep by newline
	for e in elves:
		if e != '\n':
			sum += int(e)
		else:
			# add total to new list
			rations.append(sum)
			sum = 0
	# get top n 
	total = 0
	for i in range(3):
		total += max(rations)
		print(str(i+1)+'.', max(rations))
		rations.remove(max(rations))
	print('Total:', total)
