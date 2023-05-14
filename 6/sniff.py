#!/usr/bin/python3

with open('packets.txt', 'r') as f:
    packets = f.readlines()[0].strip('\n')
    for i in range(len(packets)):
        check = set(packets[i:i+4])
        if len(check) == 4:
            print(i+4)
            break
    print(check) 


