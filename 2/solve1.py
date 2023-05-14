#!/bin/python3

# A/X = Rock, B/Y = Paper, C/Z = Scissors

with open("guide.txt", "r") as file:
	guide = file.readlines()

total = 0
for line in guide:
	score = 0
	plays = line.strip('\n').split(' ')
	if plays[1] == 'X':
		score += 1
		if plays[0] == 'A': score += 3
		elif plays[0] == 'B': score += 0
		elif plays[0] == 'C': score += 6
	elif plays[1] == 'Y':
		score += 2
		if plays[0] == 'B': score += 3
		elif plays[0] == 'C': score += 0
		elif plays[0] == 'A': score += 6
	elif plays[1] == 'Z':
		score += 3
		if plays[0] == 'C': score += 3
		elif plays[0] == 'A': score += 0
		elif plays[0] == 'B': score += 6
	else:
		print("huh")
		break
	total += score
print('Total score:', total)
