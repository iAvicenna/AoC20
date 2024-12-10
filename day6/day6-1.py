#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:44:28 2020

@author: avicenna
"""

with open('input.txt','r') as file:
    lines = file.readlines()


I = [-1] + [ind for ind,line in enumerate(lines) if line =='\n'] + [len(lines)]

groups = [''.join(lines[i+1:j]) for i,j in zip(I[0:-1],I[1:])]

count = 0

for group in groups:

    split_groups = group.split('\n')[0:-1]

    set0 = set(split_groups[0])
    for sg in split_groups[1:]:
        set0 = set0.union(set(sg))

    count += len(set0)