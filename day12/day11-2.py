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

class Waypoint():

    def __init__(self, direction_vec):

        self.direction_vec = direction_vec

    def rotate(self, angle, angle_dir):

        angle = float(angle)

        assert angle/90 == int(angle/90)
        assert angle_dir in ['R','L']

        if angle_dir == 'R':
            theta = -np.radians(angle)
        else:
            theta = np.radians(angle)

        c, s = np.cos(theta), np.sin(theta)
        R = np.array(((c, -s), (s, c)))

        x = self.direction_vec[1]
        y = self.direction_vec[0]

        new_vec = R @ np.array([x,y])

        self.direction_vec = np.array([new_vec[1], new_vec[0]])


waypoint_location = Waypoint(10*direction_vecs['E'] + direction_vecs['N'])

with open('input_test.txt') as file:
    lines = file.readlines()

movement = np.array([0.0,0.0])

for line in lines:
    line = line.replace('\n','')
    instruction = line[0]
    num = int(line[1:])

    if instruction in directions:
        waypoint_location.direction_vec += num*direction_vecs[instruction]
    elif instruction in ['R','L']:
        waypoint_location.rotate(num, instruction)
    elif instruction=='F':
        movement += num*waypoint_location.direction_vec

print(np.round(np.sum(np.abs(movement))))
