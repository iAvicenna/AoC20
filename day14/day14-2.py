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
        address = bin(int(''.join([x for x in mem_data.split(' = ')[0] if x.isnumeric()])))[2:].rjust(36).replace(' ','0')
        data = bin(int(mem_data.split(' = ')[1]))[2:].rjust(36).replace(' ','0')
        address = ''.join([x if y=='0' else y for x,y in zip(address,mask)])

        I = [ind for ind,x in enumerate(address) if x=='X']

        addresses = [address]

        for i in I:
            new_addresses = []
            for address in addresses:
                address1 = address[0:i] + '0' +address[i+1:]
                address2 = address[0:i] + '1' +address[i+1:]

                new_addresses.append(address1)
                new_addresses.append(address2)
            addresses = new_addresses

        for address in addresses:
            mem[address]=int(data,2)

print(np.sum(list(mem.values())))