# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 08:20:54 2024

@author: Admin

Solution for the Advent of Code 2024 Challenge
Problem: Day 5

Task: Determining the correctness of number patterns given befor/after rules
"""

import networkx as nx
import matplotlib.pyplot as plt

with open('test.txt') as f:
    inputtext = f.read()

rules,pattern = inputtext.split('\n\n')
rules = rules.split('\n')
rules = [(int(r.split('|')[0]),int(r.split('|')[1])) for r in rules]
# nodes = set([item for sub_list in rules for item in sub_list]) # unique values in rules

pattern = pattern.split('\n')
pattern = [list(map(int, p.split(','))) for p in pattern]

# start using graphs
G = nx.DiGraph(rules)
plt_fig_cnt = 1
plt.figure(plt_fig_cnt)
plt_fig_cnt += 1
nx.draw(G, with_labels=True, font_weight='bold')

# check if chain of pattern is included in graph
for p in pattern:
    construct = [(p[idx],p[idx+1]) for idx,entry in enumerate(p[:-1])]
    H = nx.DiGraph(construct)
    plt.figure(plt_fig_cnt)
    plt_fig_cnt += 1
    nx.draw(H, with_labels=True, font_weight='bold')
    
    leaves = [v for v, d in G.out_degree() if d == 0]
    all_paths = []
    for root in roots:
        paths = nx.all_simple_paths(G, root, leaves)
        all_paths.extend(paths)
    all_paths

plt.show()