# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 22:02:47 2024

@author: Admin

Solution for the Advent of Code 2024 Challenge
Problem: Day 12

Task: Findings connected areas in a 2D grid
"""

import numpy as np
#import itertools
import networkx as nx

with open('input.txt') as f:
    inputtext = f.read()
inputtext = inputtext.split('\n')
floorplan = np.array([[coord for coord in list(line)] for line in inputtext])
print(floorplan)
print()

def get_first_unvisited(v):
    poses = np.where(v==False)
    if poses[0].size == 0:
        return np.array([])
    return np.array([poses[1][0],poses[0][0]])

def get_adjacent(pos):
    unit_vectors = [np.array([1,0]),np.array([0,1]),np.array([-1,0]),np.array([0,-1])]
    return list(zip([np.array(u + pos) for u in unit_vectors],unit_vectors))


def out_of_bounds(pos,g):
    ymax,xmax = g.shape
    if pos[0] < 0 or pos[1] < 0 or pos[0] > xmax-1 or pos[1] > ymax-1:
        return True
    else:
        return False


def adjacent_area(g,this_pos,visited):
    # for first 
    # for every file in current area: check surroundings
    # mark as vistied, add one to area count
    # if edge of board or other area, add one to fence count 
    # if visited, skip
    # otherwise return as to be visited
    area_count = 1
    fence_count = []
    visited[this_pos[1]][this_pos[0]] = True
    for adj,uv in get_adjacent(this_pos):
        if out_of_bounds(adj,g):
            fence_count += [(this_pos,uv)]
            continue
        elif g[adj[1]][adj[0]] != g[this_pos[1]][this_pos[0]]:
            fence_count += [(this_pos,uv)]
            continue
        elif visited[adj[1]][adj[0]]:
            continue
        else:
            (ac,fc,vis) = adjacent_area(g,adj,visited)
            area_count += ac
            fence_count += fc
            visited |= vis
        
    return (area_count,fence_count,visited)
   

def sides_from_edges(edges): # e in format list( ([x,y] , unit_vector) )
    unit_vectors = [np.array([1,0]),np.array([0,1]),np.array([-1,0]),np.array([0,-1])]
    sides_count = 0
    for uv in unit_vectors: # all same facing edges
        this_edges = [e[0] for e in edges if np.all(e[1]==uv)]
        
        T=[np.array(el) for el in this_edges]

        x=[el[0] for el in T]
        y=[el[1] for el in T]

        xmat = np.expand_dims(np.array(x),1)-np.expand_dims(np.array(x),0)
        ymat = np.expand_dims(np.array(y),1)-np.expand_dims(np.array(y),0)
        conmat = np.abs(xmat)+np.abs(ymat)
        conmat[conmat!=1] = 0

        G = nx.from_numpy_array(conmat)
        nx.draw(G, with_labels=True)
        this_sides = len(list(nx.connected_components(G)))
        sides_count += this_sides
        
        # sides_count += 1 # there is at least one side
        # if len(this_edges) > 1:
        #     for p1,p2 in list(itertools.combinations(this_edges,2)):
        #         if np.sum(np.abs(p1-p2)) > 1:
        #             sides_count += 1 # the sides are not connected
        
    return sides_count
    
    
 
visitedplan = np.full_like(floorplan, False, dtype=bool)
total_cost = 0
total_cost_bulk = 0
next_pos = get_first_unvisited(visitedplan)
# main search program
while next_pos.size > 0:
    (ac,fc,vis) = adjacent_area(floorplan,next_pos,visitedplan)
    fences = len(fc)
    sides = sides_from_edges(fc)
    print("Area '%s' with size %d: %d fences, %d sides" % (floorplan[next_pos[1]][next_pos[0]],ac,fences,sides))
    #print(visitedplan)
    #print()
    total_cost += ac * fences
    total_cost_bulk += ac * sides
    visitedplan |= vis
    next_pos = get_first_unvisited(visitedplan)
    
print("The total cost of fencing the map is %d" % total_cost)
print("The bulk discount cost of fencing the map is %d" % total_cost_bulk)