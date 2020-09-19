# -*- coding: utf-8 -*-
import os

print("This is testexe.py!")

if os.path.isfile('test.txt'):
    print("This is content of test.txt!!!")
    with open('test.txt', 'r') as f:
        while True:
            content = f.readline()
            if content:
                print(content.strip('\n'))
            else:
                print("all are output of test.txt!")
                break

print('Over!')
