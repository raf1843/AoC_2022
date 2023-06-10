#!/usr/bin/python3.11
import sys
from functools import cmp_to_key

def cmpLists(left, right):
    # DEBUG: print("comparing", left, right)
    for j in range(len(left)):
        if j not in range(len(right)):
            return False
        if isinstance(left[j], list) or isinstance(right[j], list):
            if isinstance(right[j], int):
                check = cmpLists(left[j], [right[j]])
            elif isinstance(left[j], int):
                check = cmpLists([left[j]], right[j])
            else:
                check = cmpLists(left[j], right[j])
            if check == None:
                continue  
            else:
                return check
        # DEBUG: print("comparing", left[j], right[j])
        if left[j] < right[j]:
            # DEBUG: print("True because", left[j], '<', right[j])
            return True
        elif left[j] == right[j]:
            continue
        elif left[j] > right[j]:
            # DEBUG: print("False because", left[j], '>', right[j])
            return False
    if len(left) < len(right):
        # DEBUG: print("left ran out before right")
        return True

# parse file, packets come in pairs sep by blank line
if len(sys.argv) != 2:
    print("Usage: ./decoder.py <puzzle_file>")
    exit()
file = sys.argv[1]
lines = []
packets = []
with open(file, 'r') as f:
    lines = f.read().strip().splitlines()
for i in range(len(lines)):
    if lines[i] == '':
        continue
    packets.append(eval(lines[i]))

# add dividers
packets.append([[2]])
packets.append([[6]])

#for left in packets:
def compare(left, right):
    # DEBUG: print("Comparing", left, right)
    
    ordered = None
    # for item in left list
    for i in range(len(left)):
        # right ran out first; not ordered
        if i not in range(len(right)):
            # DEBUG: print("False because right ran out first")
            ordered = False
            break
        # both left and right are ints, simple comparison
        if isinstance(left[i], int) and isinstance(right[i], int):
            # DEBUG: print("Comparing", left[i], right[i])
            if left[i] < right[i]:
                ordered = True
                break
            elif left[i] == right[i]:
                continue
            else:
                ordered = False
                break
        # otherwise, iterative comparison
        # if only one or the other is an int, cast to list
        else:
            if isinstance(left[i], int):
                tmp = [left[i]]
                ordered = cmpLists(tmp, right[i])
            elif isinstance(right[i], int):
                tmp = [right[i]]
                ordered = cmpLists(left[i], tmp)
            else:
                ordered = cmpLists(left[i], right[i])
        if ordered == None:
            continue
        else:
            break
    # DEBUG: print(ordered)
    if ordered or ordered == None:
        #if ordered == None:
            # DEBUG: print("True because left ran out first")
        return 1
    else:
        return -1

packets = sorted(packets, key=cmp_to_key(compare), reverse=True)
print((packets.index([[2]])+1) * (packets.index([[6]])+1))
