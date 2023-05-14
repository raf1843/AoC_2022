#!/usr/bin/python3

with open('packets.txt', 'r') as f:
    packets = f.readlines()[0].strip('\n')
    for i in range(len(packets)):
        check = set(packets[i:i+14])
        if len(check) == 14:
            print(i+14)
            break
    print(check) 


