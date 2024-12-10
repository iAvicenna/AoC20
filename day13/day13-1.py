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
earliest_deps = {}
difs = {}
for bus_id in ids:
    if bus_id != 'x':
        bus_id = int(bus_id)
        div = int(dep_min/bus_id)
        earliest_deps[bus_id] = (div+1)*bus_id
        difs[bus_id] = (div+1)*bus_id - dep_min

best_bus_ind = np.argmin(list(difs.values()))
best_bus_id = list(difs.keys())[best_bus_ind]
print(difs[best_bus_id]*best_bus_id)