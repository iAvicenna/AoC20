#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:44:28 2020

@author: avicenna
"""


with open('input.txt','r') as file:
    lines = file.readlines()

nums = [int(x) for x in lines]
min_num = min(nums)
max_num = max(nums)

for ind1,num1 in enumerate(nums):

    if num1 <= 2020 - min_num and num1 >= 2020 - max_num:

        for num2 in nums[ind1:]:

            if num1 + num2 == 2020:
                print(f'num1: {num1}, num2: {num2}, product: {num1*num2}')
