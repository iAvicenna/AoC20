#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 11:21:10 2020

@author: avicenna
"""
import numpy as np

with open('input.txt','r') as file:
    lines = file.readlines()

numbers = [int(x) for x in lines[0].split(',')]

stop = False
counter = 0

len_array = max(numbers)
number_turns = [[]]*(len_array+1)

for ind,number in enumerate(numbers,start=1):
    number_turns[number] = [ind]

last_number = numbers[-1]
N = 30000000

for i in range(len(numbers)+1, N+1):

    if len(number_turns) < last_number+1:
        number_turns += (last_number - len(number_turns) + 1)*[[]]

    if len(number_turns[last_number])==1:
        last_number = 0
        if len(number_turns[0])>0:
            number_turns[0].append(i)
        else:
            number_turns[0] = [i]
    elif len(number_turns[last_number])>1:
        last_number = number_turns[last_number][-1] - number_turns[last_number][-2]

        if len(number_turns) < last_number+1:
            number_turns += (last_number + 1 - len(number_turns))*[[]]

        if len(number_turns[last_number])>0:
            number_turns[last_number].append(i)
        else:
            number_turns[last_number] = [i]
    else:
        number_turns[last_number] = [i]

    if len(number_turns[last_number])>2:
        number_turns[last_number] = number_turns[last_number][-2:]

    if i%10000==3 or i == N:
        complete = np.round(i/N,3)
        print(f'{complete}- {last_number}')
