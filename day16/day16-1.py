#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 12:41:33 2020

@author: avicenna
"""

with open('input.txt', 'r') as file:
    lines = file.readlines()

I = [ind for ind,line in enumerate(lines) if line=='\n']
I = [-1] + I + [len(lines)]

split_data = [lines[i+1:j] for i,j in zip(I[0:-1],I[1:])]

rules = {}

for rule in split_data[0]:
    split_rule = [x.split(' or ') for x in rule.split(':')]
    split_rule = [x.replace(' ','') for sublist in split_rule for x in sublist]

    rules[split_rule[0]] = []

    for val_range in split_rule[1:]:
        val_start = int(val_range.split('-')[0])
        val_end = int(val_range.split('-')[1])

        rules[split_rule[0]] += list(range(val_start,val_end+1))

complete_range = []

for rule_range in rules.values():
    complete_range += rule_range

sum_error = 0

for ticket in split_data[2][1:]:
    numbers = [int(x) for x in ticket.split(',')]

    I = [number for number in numbers if number not in complete_range]

    sum_error += sum(I)

