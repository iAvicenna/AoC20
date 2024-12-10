#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 13:07:09 2020

@author: avicenna
"""
import numpy as np
from itertools import product

class Grid():

    def __init__(self, coords, state,  n_rows, ncols):

        self.coords = coords

        assert state in ['.','#','L'] #0: floor, 1:full, 2:empty

        self.state = state

        self.ncoordinates = []

        row_min = max([0, coords[0]-1])
        row_max = min([n_rows-1, coords[0]+1])
        col_min = max([0, coords[1]-1])
        col_max = min([n_cols-1, coords[1]+1])

        row_range = list(range(row_min, row_max+1, 1))
        col_range = list(range(col_min, col_max+1, 1))

        self.ncoords = [list(x) for x in product(row_range, col_range) if list(x) != coords ]

class Grids():

    def __init__(self, grid_list, n_rows, ncols):

        assert len(grid_list) == n_rows
        assert all(len(x) == n_cols for x in grid_list)
        self.grid_list = grid_list
        self.n_rows = n_rows
        self.n_cols = n_cols

    def return_states(self):

        states = []

        for irow in range(self.n_rows):
            states.append([])
            for icol in range(self.n_cols):
                states[irow].append([])
                states[irow][icol] = self.grid_list[irow][icol].state

        return states

    def print_states(self):

        states = self.return_states()

        for irow in range(self.n_rows):
            for icol in range(self.n_cols):
                print(states[irow][icol], end='')
            print('')
        print('\n')

    def number_of_occupied_seats(self):

        no = 0

        for grid_row in self.grid_list:
            for grid in grid_row:
                if grid.state == '#':
                    no += 1

        return no



    def update(self):

        new_grid_list = []

        for irow in range(self.n_rows):

            new_grid_list.append([])

            for icol in range(self.n_cols):

                new_grid_list[irow].append([])

                grid = self.grid_list[irow][icol]

                if grid.state == '.':
                    new_grid_list[irow][icol] = grid
                else:

                    states = [self.grid_list[ncoord[0]][ncoord[1]].state for ncoord in grid.ncoords]

                    if grid.state == 'L' and states.count('#') == 0:
                        new_grid_list[irow][icol] = Grid([irow, icol], '#', self.n_rows, self.n_cols)

                    elif grid.state == '#' and states.count('#') >= 4:
                        new_grid_list[irow][icol] = Grid([irow, icol], 'L', self.n_rows, self.n_cols)
                    else:
                        new_grid_list[irow][icol] = grid


        self.grid_list = new_grid_list

with open('input.txt') as file:
    lines = file.readlines()

lines = [line.replace('\n','') for line in lines]

n_rows = len(lines)
n_cols = len(lines[0])
grids = []

for irow in range(n_rows):

    grids.append([])

    for icol in range(n_cols):

        grids[irow].append(Grid([irow, icol], lines[irow][icol], n_rows, n_cols))

grids = Grids(grids, n_rows, n_cols)
stop = False
states = []
counter = 0
while not stop:
    states.append(grids.return_states())
    #grids.print_states()

    grids.update()
    states.append(grids.return_states())
    counter += 1

    is_equal = all(x==y for x,y in zip(states[-1],states[-2]))
    print(counter)
    if is_equal:
        stop = True
        print(grids.number_of_occupied_seats())

