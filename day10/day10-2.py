#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 11:28:14 2020

@author: avicenna
"""

import numpy as np
import sys
import os

script_path = os.path.realpath(__file__)
parent_path = os.path.dirname(os.path.dirname(script_path))

sys.path.append(parent_path)
from Tools import Graph

with open('input.txt','r') as file:
    lines = file.readlines()

jolts = []

for line in lines:
    jolts.append(int(line.replace('\n','')))

device_jolt = max(jolts) + 3
jolts.append(0)
jolts.append(device_jolt)
jolts = np.sort(np.array(jolts))
graph = Graph()
for jolt in jolts:
    graph.add_node(jolt)


for ind,jolt in enumerate(jolts):
    min_jolt = jolt + 1
    max_jolt = jolt + 3

    I = np.where([x >= min_jolt and x <= max_jolt for x in jolts[ind:]])[0]

    for i in I:
        graph.connect_nodes(jolt, jolts[i+ind], one_directional=True)

#find all paths between first and last node exhaustively would take too long
#because there are 173625106649344 paths. Insted we break the graph into multiple
#parts, find the number of paths for each part and take product of number of paths.
#this breaking can be done in nodes in which the adjacency set of this node has 3 elements
#and adjacency set of the previous two nodes has just 1 element
#
#More in general one could use nodes which have to exist in every path from
#start to end, though not sure how to detect this for a general graph.


admissible_nodes = []
nodes = list(graph.adjacency_set.keys())
for ind,node2 in enumerate(nodes[2:-1],start=2):
    node0 = nodes[ind-2]
    node1 = nodes[ind-1]

    vals0 = graph.adjacency_set[node0]
    vals1 = graph.adjacency_set[node1]
    vals2 = graph.adjacency_set[node2]

    if len(vals2)==3 and set(vals1) == set([node2]) and set(vals0) == set([node1]):
        admissible_nodes.append(node2)


nums = [jolts[0]] + admissible_nodes + [jolts[-1]]
path_lens = np.zeros((len(nums)-1,))
paths = [[]]*(len(nums)-1)

for i in range(len(nums)-1):
    paths[i] = graph.find_all_paths(nums[i],nums[i+1])
    path_lens[i] = len(paths[i])

print(np.prod(path_lens))