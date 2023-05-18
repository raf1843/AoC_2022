#!/usr/bin/python3

def toss(toss, div, tossT, tossF):
    if toss % div == 0:
        if tossT in items:
            items[tossT].append(toss)
        else:
            items.update({tossT: [toss]})
    else:
        if tossF in items:
            items[tossF].append(toss)
        else:
            items.update({tossF: [toss]})

lines = []
with open('puzzle.txt', 'r') as file:
    lines = file.read().splitlines()

idx = 0
items = {} 
monkeys = {}
ops = {}
divs = {}
tosses = {}
for line in lines:
    if "Monkey" in line:
        idx = int(line.split()[1].strip(':'))
        if idx not in items:
            items.update({idx: []})
        if idx not in monkeys: 
            monkeys.update({idx: 0})
        continue
    elif "Starting items" in line:
        temp = line.split(':')[1].split(',')
        for t in temp:
            items[idx].append(int(t))
        continue
    elif "Operation" in line:
        op = line.split(':')[1].split('=')[1].split()
        ops.update({idx: op})
    elif "Test" in line:
        # only test seems to be divisible
        if "divisible" in line:
            div = int(line.split()[3])
            divs.update({idx: div})
        continue
    elif "true" in line:
        tosses.update({idx: [-1, -1]})
        tosses[idx][0] = int(line.split()[-1])
        continue
    elif "false" in line:
        tosses[idx][1] = int(line.split()[-1])
        continue

# rounds
for r in range(20):
    for idx in monkeys: 
        # Inspect
        operand1, operand2 = ops[idx][0], ops[idx][2]
        for l in range(len(items[idx])):
        # generalized a little but assumed operation always assigned to new
            if ops[idx][0] == "old":
                operand1 = items[idx][l]
            if ops[idx][2] == "old":
                operand2 = items[idx][l]
            # operations
            if ops[idx][1] == '+':
                items[idx][l] = int(operand1) + int(operand2)
            elif ops[idx][1] == '-':
                items[idx][l] = int(operand1) - int(operand2)
            elif ops[idx][1] == '*':
                items[idx][l] = int(operand1) * int(operand2)
            elif ops[idx][1] == '/':
                items[idx][l] = int(operand1) / int(operand2)
            items[idx][l] //= 3
            monkeys[idx] += 1
            # Test
            toss(items[idx][l], divs[idx], tosses[idx][0], tosses[idx][1])
        items[idx].clear()
#print(items)
#print(monkeys)
total = 1
monke = list(monkeys.values())
monke.sort(reverse=True)
most = monke[:2]
for m in most:
    total *= m
print("Monkey Business:", total)
