#!/bin/python3

# A = Rock, B = Paper, C = Scissors
# X = Lose, Y = Draw, Z = Win

with open("guide.txt", "r") as file:
	guide = file.readlines()

total = 0
for line in guide:
	score = 0
	plays = line.strip('\n').split(' ')
	# X = 
	if plays[1] == 'X':
		score += 0
		# lose, so A means play C = 3 points, etc
		if plays[0] == 'A': score += 3
		elif plays[0] == 'B': score += 1
		elif plays[0] == 'C': score += 2
	elif plays[1] == 'Y':
		score += 3
		if plays[0] == 'A': score += 1
		elif plays[0] == 'B': score += 2
		elif plays[0] == 'C': score += 3
	elif plays[1] == 'Z':
		score += 6
		if plays[0] == 'A': score += 2
		elif plays[0] == 'B': score += 3
		elif plays[0] == 'C': score += 1
	else:
		print("huh")
		break
	total += score
print('Total score:', total)
