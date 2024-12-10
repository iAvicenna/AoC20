#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 03:04:45 2020

@author: avicenna
"""
import numpy as np

with open('input.txt') as f:
    lines = f.readlines()

dep_min = int(lines[0])
ids = lines[1].split(',')
difs = []
valid_bus_ids = []
counter = 0
for bus_id in ids:
    if bus_id != 'x':
        difs.append(counter)
        valid_bus_ids.append(int(bus_id))

    counter += 1

power = len(valid_bus_ids)
max_dif = max(difs)
id_product = np.product(valid_bus_ids)
counter = id_product
stop = False
loop_counter = 0
while not stop:

    val1 = int(np.power(counter, 1/power) - max_dif)
    val2 = int(np.power(counter, 1/power))

    for val in range(val1,val2+1):
        prod_val = np.product([val + x for x in difs])
        if prod_val == counter:
            stop = True
            print(val)

    print(loop_counter)
    counter += id_product
    loop_counter += 1