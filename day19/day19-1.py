#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 22:52:02 2020

@author: avicenna
"""
from itertools import product
with open('input_test.txt','r') as file:
    lines = file.readlines()

lines = [line.replace('\n','') for line in lines]

rules = {}
I = lines.index('')
end_nodes = []
for line in lines[:I]:
    no = int(line.split(':')[0])
    rule = line.split(':')[1][1:]
    rules[no] = rule
    if '"' in rule:
        end_nodes.append(no)

def construct_rule(no):

    rule = rules[no]
    all_rules = []
    if '"' not in rule and '|' not in rule:

        rules1 = [int(x) for x in rule.split(' ')]

        for ind1,rule1 in enumerate(rules1):
            if ind1==0:
                all_rules = construct_rule(rule1)
            else:
                new_rules = product(all_rules,construct_rule(rule1))
                all_rules = [x+y for x,y in product(new_rules,all_rules)]

    elif '|' in rule:

        rules1 = [int(x) for x in rule.split(' | ')[0].split(' ')]
        rules2 = [int(x) for x in rule.split(' | ')[1].split(' ')]

        for ind1,rule1 in enumerate(rules1):
            if ind1==0:
                all_rules = construct_rule(rule1)
            else:
                all_rules = [x+y for x,y in product(all_rules,construct_rule(rule1))]
        for ind1,rule2 in enumerate(rules2):

                all_rules = [x+y for x,y in product(all_rules,construct_rule(rule2))]


    elif '"' in rule:
        return rule[1]

    return all_rules

all_rules = construct_rule(0)

