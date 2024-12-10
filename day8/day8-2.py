#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:44:28 2020

@author: avicenna
"""

import numpy as np


with open('input.txt','r') as file:
    lines = file.readlines()

I = [ind for ind,line in enumerate(lines) if 'jmp' in line or 'nop' in line]

for chng_ind in I:

    global_var = 0

    visited = np.zeros((len(lines),),dtype=bool)
    ind = 0
    stop = False
    is_finished = False
    while not stop:
        if visited[ind] == True:
            break


        line = lines[ind]
        comm = line.split(' ')[0]
        incr = int(line.split(' ')[1])

        if ind == chng_ind:
            if comm == 'jmp':
                comm = 'nop'
            elif comm == 'nop':
                comm = 'jmp'
            else:
                print('Error')

        visited[ind] = True


        if comm =='acc':
            global_var += incr
            ind += 1
        elif comm =='jmp':
            ind += incr
        else:
            ind += 1

        if ind == len(lines):
            is_finished = True
            stop = True

    if is_finished:
        print(global_var)