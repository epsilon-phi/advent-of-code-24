# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 22:07:55 2024

@author: Admin

Solution for the Advent of Code 2024 Challenge
Problem: Day 10

Task: Finding paths on a topographical map
"""

import numpy as np
import networkx as nx

with open('input.txt') as f:
    inputtext = f.read()

def enumerate_grid(g):
    res = []
    for y,row in enumerate(g):
        for x,elem in enumerate(row):
            res.append(((x,y),elem))
    return res

def adjacent_grid(g,x,y):
    ymax,xmax = g.shape
    res = []
    if x > 0: # look bevore in x direction
        res.append(((x-1,y),g[y][x-1]))
    if y > 0: # look bevore in y direction
        res.append(((x,y-1),g[y-1][x]))
    if x < xmax-1: # look bevor in x direction
        res.append(((x+1,y),g[y][x+1]))
    if y < ymax-1: # look bevor in x direction
        res.append(((x,y+1),g[y+1][x]))
    return res


inputtext = inputtext.split('\n')
topo = np.array([[int(coord) for coord in list(line)] for line in inputtext])

# strategy: build map as directed graph, where the nodes are the unique tupels of coordinates
# create the height map as a dictionary
heightmap = {}
graphplist = []
for coord,elem in enumerate_grid(topo):
    heightmap[coord] = elem
    # always add valid edges to next higher nodes
    for acoord,adj in adjacent_grid(topo,*coord):
        if adj == (elem+1):
           graphplist.append((coord,acoord))    
        
G = nx.DiGraph(graphplist)
nx.set_node_attributes(G, heightmap, 'height')
pos = dict(zip(list(G.nodes), list(G.nodes)))
nx.draw(G,pos,labels=nx.get_node_attributes(G, 'height') )

trailends = [node for node in G.nodes() if G.in_degree(node)!=0 and G.out_degree(node)==0 and G.nodes[node]['height']==9]
trailstarts = [node for node in G.nodes() if G.nodes[node]['height']==0]

# now check if there is any connection between a start and all ends and count
# for part 2: generate all paths between a start and an end and count, hopefully... 
scores = {}
ratings = {}
for trailstart in trailstarts:
    scores[trailstart] = 0
    ratings[trailstart] = 0
    for trailend in trailends:
        if nx.has_path(G,trailstart,trailend):
            scores[trailstart] += 1
            all_paths = list(nx.all_simple_paths(G,trailstart,trailend))
            ratings[trailstart] += len(all_paths)
        

total_score = np.sum([scores[s] for s in scores])
total_rating = np.sum([ratings[r] for r in ratings])

print("The total score of the map is %d" % total_score)
print("The total rating of the map is %d" % total_rating)
