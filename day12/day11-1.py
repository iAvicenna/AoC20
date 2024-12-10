#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 13:07:09 2020

@author: avicenna
"""
import numpy as np

direction_vecs = {
    'E':np.array([0,1]),
    'S':np.array([-1,0]),
    'W':np.array([0,-1]),
    'N':np.array([1,0])
    }

directions=list(direction_vecs.keys())


class Direction():

    def __init__(self, direction):

        assert direction in ['W','N','E','S']

        self.direction = direction
        self.direction_vec = direction_vecs[direction]

    def rotate(self, angle, angle_dir):

        angle = float(angle)

        assert angle/90 == int(angle/90)
        assert angle_dir in ['R','L']

        index = directions.index(self.direction)

        if angle_dir == 'R':
            angle_dir = 1
        else:
            angle_dir = -1

        new_index = (index + angle_dir*int(angle/90))%4

        self.direction = directions[new_index]
        self.direction_vec = direction_vecs[directions[new_index]]


ship_direction = Direction('E')

with open('input.txt') as file:
    lines = file.readlines()

movement = np.array([0,0])

for line in lines:
    line = line.replace('\n','')
    instruction = line[0]
    num = int(line[1:])

    if instruction in directions:
        movement += num*direction_vecs[instruction]
    elif instruction in ['R','L']:
        ship_direction.rotate(num, instruction)

    elif instruction=='F':
        movement += num*ship_direction.direction_vec

print(np.sum(np.abs(movement)))
