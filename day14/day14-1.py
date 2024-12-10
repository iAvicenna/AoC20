#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 03:04:45 2020

@author: avicenna
"""
import numpy as np

with open('input.txt') as f:
    lines = f.readlines()

lines = [line.replace('\n','') for line in lines]

break_indices = [ind for ind,x in enumerate(lines) if 'mask' in x] + [len(lines)]


data_groups = [lines[i:j] for i,j in zip(break_indices[0:-1],break_indices[1:])]
mem = {}
for data_group in data_groups:
    mask = ''.join([x for x in data_group[0] if x.isnumeric() or x=='X'])


    for mem_data in data_group[1:]:
        address = int(''.join([x for x in mem_data.split(' = ')[0] if x.isnumeric()]))
        data = bin(int(mem_data.split(' = ')[1]))[2:].rjust(36).replace(' ','0')
        data = ''.join(x if y=='X' else y for x,y in zip(data,mask))
        mem[address]=int(data,2)

print(np.sum(list(mem.values())))
