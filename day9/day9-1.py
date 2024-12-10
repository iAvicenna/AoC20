#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:44:28 2020

@author: avicenna
"""

import numpy as np
from itertools import product
global_var = 0

with open('input.txt','r') as file:
    lines = file.readlines()

numbers = []

for line in lines:
    numbers.append(int(line.replace('\n','')))

def is_sum(numbers2, number):
    for num1,num2 in product(numbers2,numbers2):
        if num1 + num2 == number:
            return True

    return False

for i in range(25,len(numbers)):
    numbers25 = numbers[i-25:i]
    next_number = numbers[i]

    if not is_sum(numbers25, next_number):
        print(f'{next_number} can not be expressed as a sum')