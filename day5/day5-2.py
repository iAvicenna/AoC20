#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:44:28 2020

@author: avicenna
"""
import numpy as np

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

full_seats = np.zeros((np.max(rows)+1,np.max(seats)+1), dtype=bool)

for row,col in zip(rows,seats):
    full_seats[row,col] = True


for i in range(np.max(rows)+1):
    if i>0 and i<np.max(rows):
        seat_row = full_seats[i,:]
        I = seat_row == False
        if True in I:
            missing_col = list(I).index(True)
            missing_row = i
            missing_id = missing_row*8 + missing_col