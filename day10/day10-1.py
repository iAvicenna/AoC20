#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 11:28:14 2020

@author: avicenna
"""

import numpy as np
from itertools import product

with open('input.txt','r') as file:
    lines = file.readlines()

jolts = []

for line in lines:
    jolts.append(int(line.replace('\n','')))

device_jolt = max(jolts) + 3

jolts = np.array(jolts)
stop = False
min_jolt = 1
max_jolt = 3
current_jolt = 0
one_dif = 0
three_dif = 0
sequence = [0]
while not stop:
    I = np.where([x >= min_jolt and x <= max_jolt for x in jolts])[0]
    I = I[np.argmin(jolts[I])]

    dif = -current_jolt + jolts[I]
    current_jolt = jolts[I]
    sequence.append(current_jolt)

    if dif == 1:
        one_dif += 1
    elif dif == 3:
        three_dif +=  1

    max_jolt = current_jolt + 3
    min_jolt = current_jolt + 1

    jolts = np.delete(jolts, I)

    if device_jolt - current_jolt <=3:
        stop = True

        if device_jolt - current_jolt == 3:
            three_dif += 1
        if device_jolt - current_jolt == 1:
            one_dif += 1

print(one_dif*three_dif)