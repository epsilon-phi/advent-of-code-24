# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 08:20:54 2024

@author: Admin

Solution for the Advent of Code 2024 Challenge
Problem: Day 5

Task: Determining the correctness of number patterns given befor/after rules
"""

import math
import networkx as nx

with open('input.txt') as f:
    inputtext = f.read()

rules,pattern = inputtext.split('\n\n')
rules = rules.split('\n')
rules = [(int(r.split('|')[0]),int(r.split('|')[1])) for r in rules] 

pattern = pattern.split('\n')
pattern = [list(map(int, p.split(','))) for p in pattern]

G = nx.DiGraph(rules) # create graph which encodes the rules

def middle_entry(l):
    return l[math.floor(len(l)/2)]

middle_num_sum = 0
corrected_sum = 0
for p in pattern:  
    if nx.is_path(G,p): # check if this pattern is a valid path in graph
        middle_num_sum += middle_entry(p)
    else:
        J = G.subgraph(p)
        corrected_p = nx.dag_longest_path(J)
        corrected_sum += middle_entry(corrected_p)

print("Sum of middle numbers of correct patterns %d" % middle_num_sum)
print("Sum of middle numbers of correct-ed patterns %d" % corrected_sum)