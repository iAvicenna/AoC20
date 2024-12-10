#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:44:28 2020

@author: avicenna + graph path finding algorithms from: https://www.python.org/doc/essays/graphs/
"""



class BagGraph():

    def __init__(self):
        self._node_map = {}
        self._number_of_nodes = 0
        self.adjacency_set = {}
        self.weights = {}

    def get_nodes(self):
        return list(self._node_map.keys())

    def add_node(self,node_name):

        if node_name not in self._node_map:
            self._node_map[node_name] = self._number_of_nodes
            self._number_of_nodes += 1
            self.adjacency_set[node_name] = []

    def connect_nodes(self, node_name1, node_name2, one_directional=False):

        assert node_name1 in self._node_map, f'{node_name1} not in graph'
        assert node_name2 in self._node_map, f'{node_name2} not in graph'


        if not one_directional and node_name1 not in self.adjacency_set[node_name2]:
            self.adjacency_set[node_name2].append(node_name1)
        if node_name2 not in self.adjacency_set[node_name1]:
            self.adjacency_set[node_name1].append(node_name2)

    def set_weight(self, node_name1, node_name2, weight):

        assert node_name2 in self.adjacency_set[node_name1], 'node_name2 is not in adjacency set of node_name1'

        self.weights[(node_name1, node_name2)] = weight

    def find_path(self, start, end, path=[]):
        path = path + [start]
        graph = self.adjacency_set
        if start == end:
            return path
        if start not in graph:
            return None
        for node in graph[start]:
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath: return newpath
        return None

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        graph = self.adjacency_set
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


with open('input.txt','r') as file:
    lines = file.readlines()

set_dict = {}

graph = BagGraph()

for line in lines:
    split_lines = line.replace('\n','').split(' contain ')
    sup_set = ''.join(split_lines[0].split(' ')[-3:-1])
    sub_set = [''.join(x.split(' ')[-3:-1]) for x in split_lines[1].split(',')]
    weights = [int(x) for x in line if x.isdigit()]

    graph.add_node(sup_set)

    if 'noother' in sub_set:
        sub_set.pop(sub_set.index('noother'))

    for ind,colour in enumerate(sub_set):
        graph.add_node(colour)
        graph.connect_nodes(sup_set, colour, one_directional=True)
        graph.set_weight(sup_set, colour, weights[ind])

end = 'shinygold'
paths = []
max_len = 0

for node in graph.get_nodes():
    if node != 'shinygold':
        all_paths = graph.find_all_paths('shinygold', node)

        if len(all_paths)>0:
            for path in all_paths:
                paths.append(path)

numbers = {}

for path in paths:
    number = 1

    for ind,node1 in enumerate(path[0:-1]):
        node2 = path[ind+1]
        number *= graph.weights[(node1,node2)]

        numbers[''.join(path[0:ind+2])] = number

sum_count = sum(list(numbers.values()))

