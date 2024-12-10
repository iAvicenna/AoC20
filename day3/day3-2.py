#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:44:28 2020

@author: avicenna
"""
import numpy as np

with open('input.txt','r') as file:
    lines = file.readlines()

d_h = len(lines)
d_w = len(lines[0])-1

tree_map = np.zeros((d_h, d_w), dtype=bool)
for ind,line in enumerate(lines):
    I = np.array([False if x =='.' else True for x in line[0:-1]])
    tree_map[ind, I] = 1

vectors = [np.array([1, 1]),
           np.array([1, 3]),
           np.array([1, 5]),
           np.array([1, 7]),
           np.array([2, 1])]

count = []
prod = 1

for vector in vectors:
    car_coordinates = np.array([0, 0])
    car_map = np.zeros((d_h, d_w), dtype=bool)

    while car_coordinates[0] < d_h:
        car_map[car_coordinates[0],car_coordinates[1]] = True
        car_coordinates += vector
        car_coordinates[1] = car_coordinates[1]%d_w

    count.append(np.count_nonzero(car_map*tree_map))
    prod *= count[-1]

print(count)
print(prod)