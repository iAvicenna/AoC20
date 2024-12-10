#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 12:41:33 2020

@author: avicenna
"""

import numpy as np

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
rule_keys = list(rules.keys())
key_positions = {}


for ticket in split_data[2][1:]:
    numbers = [int(x) for x in ticket.split(',')]
    len_numbers = len(numbers)
    if any(x in complete_range for x in numbers):

        for ind1,number in enumerate(numbers):

            if ind1 not in key_positions:
                key_positions[ind1] = []

            indices = [ind for ind, rule_range in enumerate(rules.values()) if number in rule_range]

            if len(indices)==1 or len(key_positions[ind1])==0:

                key_positions[ind1] = [rule_keys[x] for x in indices]
            elif len(indices)>0:
                key_positions[ind1] = list(set(key_positions[ind1]).intersection([rule_keys[x] for x in indices]))

while any( len(x)>1 for x in key_positions.values() ):

    I = [x for ind,x in enumerate(key_positions.values()) if len(x)==1]
    I = [x for sublist in I for x in sublist]
    for key in key_positions:
        if len(key_positions[key])>1:
            key_positions[key] = set(key_positions[key]).difference(I)


my_ticket_numbers = [int(x) for x in split_data[1][1].split(',')]

I = [ind for ind,x in enumerate(key_positions) if 'departure' in list(key_positions[x])[0]]

departure_numbers = [my_ticket_numbers[x] for x in I]

print(np.product(departure_numbers))