#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:44:28 2020

@author: avicenna
"""

import numpy as np

global_var = 0

with open('input.txt','r') as file:
    lines = file.readlines()

visited = np.zeros((len(lines),),dtype=bool)

ind = 0
stop = False
while not stop:
    if visited[ind] == True:
        break

    line = lines[ind]
    comm = line.split(' ')[0]
    incr = int(line.split(' ')[1])
    visited[ind] = True

    print (comm,incr)

    if comm =='acc':
        global_var += incr
        ind += 1
    elif comm =='jmp':
        ind += incr
    else:
        ind += 1