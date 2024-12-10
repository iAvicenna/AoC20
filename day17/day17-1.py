#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 13:56:41 2020

@author: avicenna
"""

import sys
import numpy as np
sys.path.append('../')

from Tools import Graph

class CubeGraph(Graph):

    def __init__(self, N, states):
        super(CubeGraph, self).__init__()
        self.dim = N
        self.states = states

    def connect_neighbours(self):

        nodes = self.get_nodes()
        N = self.dim
        for node in nodes:

            min_x = max([node[0]-1,0])
            min_y = max([node[1]-1,0])
            min_z = max([node[2]-1,0])
            max_x = min([node[0]+1, N-1])
            max_y = min([node[1]+1, N-1])
            max_z = min([node[2]+1, N-1])

            for i in range(min_x, max_x+1):
                for j in range(min_y, max_y+1):
                    for k in range(min_z, max_z+1):

                        if (i,j,k) in nodes and (i,j,k) != node:
                            self.connect_nodes(node, (i,j,k))

    def connect_nodes(self, node_name1, node_name2):

        self.adjacency_set[node_name1].append(node_name2)

    def update(self,zrange):

        nodes = self.get_nodes()
        graph = self.adjacency_set
        new_states = self.states.copy()
        for node in nodes:
            if node[2] in zrange:
                adjacent_nodes = graph[node]

                I = len([x for x in adjacent_nodes if self.states[x]=='#'])

                if self.states[node] == '#' and I != 2 and I != 3:
                    new_states[node] = '.'


                elif self.states[node] == '.' and I==3:
                    new_states[node] = '#'

        self.states = new_states.copy()

    def print_state(self, states=None):

        if states is None:
            states = self.states

        for j in range(self.dim):
            if not all([x=='.' for x in states[:,:,j].flatten()]):
                print(f'z={j}')
                for i in range(self.dim):
                    print(''.join([x for x in states[i,:,j]]))
                print('\n')
        print('\n')

    def count_active(self):

        nodes = self.get_nodes()
        count = 0


        for node in nodes:
            if self.states[node] == '#':
                count += 1

        return count


with open('input.txt','r') as file:
    lines = file.readlines()

lines = [line.replace('\n','') for line in lines]

turns = 6
dim = len(lines)
initial = turns+1
N = initial + dim + turns + 1

states = np.zeros((N,N,N), dtype=str)
inactive_slice = [['.']*N]*N

state0 = [[]]*N

for i in range(N):

    state0[i] = ['.']*N

for i in range(initial,initial+dim):
    for j in range(initial,initial+dim):
        state0[i][j] = lines[i-initial][j-initial]

for ind in range(N):
    states[ind,:,initial] = np.array([x for x in state0[ind]])
    for j in range(N):
        if j != initial:
            states[ind,:,j] = np.array([x for x in inactive_slice[ind]])


s1 = N
s2 = N
s3 = N
cubes = CubeGraph(N, states)

for k in range(s1):
    for j in range(s2):
        for i in range(s3):
            cubes.add_node((i,j,k))

cubes.print_state()
cubes.connect_neighbours()

for i in range(6):
    print(f'cycle {i+1}')
    cubes.update(range(initial-i-1,initial+i+2))
    cubes.print_state()

    print(cubes.count_active())
#422 not right