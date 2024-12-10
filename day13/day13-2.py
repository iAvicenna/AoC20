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
        difs.append( counter%int(bus_id))
        valid_bus_ids.append(int(bus_id))

    counter += 1
rems = [(bus_id - dif%bus_id)%bus_id for dif,bus_id in zip(difs,valid_bus_ids)]
I = np.argsort(valid_bus_ids)
valid_bus_ids = sorted(valid_bus_ids)
rems = [rems[x] for x in I]
product = np.product(valid_bus_ids)

stop_while = False
i = 0
loop_index = 0
start = rems[0]
step = 1
stop = valid_bus_ids[0]
num1 = valid_bus_ids[0]
rem1 = rems[0]
found=False

while not stop_while:
    for num in range(start,stop,step):
        if num%num1 == rem1:
            print(num)
            found = True
            step = step*valid_bus_ids[0]

            valid_bus_ids.pop(0)
            rems.pop(0)

            if len(valid_bus_ids)==0:
                stop_while = True
                print(num)

            else:
                stop = stop*valid_bus_ids[0]
                start = num
                num1 = valid_bus_ids[0]
                rem1 = rems[0]
            break

    loop_index += 1
    if not found:
        raise ValueError('Common multiple with remainder not found, something wrong')

#836524002700652 too high