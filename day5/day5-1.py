#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:44:28 2020

@author: avicenna
"""


with open('input.txt','r') as file:
    lines = file.readlines()

rows = []
seats = []
ids = []
for line in lines:
    row = int(line[0:7].replace('B','1').replace('F','0'),2)
    seat = int(line[7:].replace('R','1').replace('L','0'),2)

    rows.append(row)
    seats.append(seat)
    ids.append(row*8 + seat)



