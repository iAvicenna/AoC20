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

wrong_number = None
wrong_ind = None
for i in range(25,len(numbers)):
    numbers25 = numbers[i-25:i]
    next_number = numbers[i]

    if not is_sum(numbers25, next_number):
        wrong_number = next_number
        wrong_index = i
        break

for i in range(wrong_index):

    for j in range(i, wrong_index):
        sum_val = sum(numbers[i:j])

        if sum_val == wrong_number:
            result = min(numbers[i:j]) + max(numbers[i:j])
            print(f'{result}')
