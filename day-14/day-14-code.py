# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 22:18:00 2024

@author: Admin

Solution for the Advent of Code 2024 Challenge
Problem: Day 14

Task: Calculating positions ob objects in a wraparound 2D grid
"""

import numpy as np
import networkx as nx
import re

xmax = 11#101
ymax = 7#103
steps = 100

with open('test.txt') as f:
    inputtext = f.read()
    
poses = []
velos = []    
for idx,line in enumerate(inputtext.split('\n')):
    parts = line.split(' ')
    posx = int(re.findall('(?<=)[\d-]+(?=,)', parts[0])[0])
    posy = int(re.findall('(?<=,)[\d-]+', parts[0])[0])
    velx = int(re.findall('(?<=)[\d-]+(?=,)', parts[1])[0])
    vely = int(re.findall('(?<=,)[\d-]+', parts[1])[0])
    poses.append(posx+posy*1j)
    velos.append(velx+vely*1j) 
 
def finalpos(p,v):
    fc = p + v * steps     
    fx = fc.real % xmax
    fy = fc.imag % ymax 
    return fx + fy*1j
 
def getgrid(poses):
    grid = np.zeros((ymax,xmax),dtype=int) 
    for p in poses:
        grid[int(p.imag)][int(p.real)] += 1
    return grid

def safetyfactor(poses):
    grid = getgrid(poses)
    q1 = np.sum(grid[:int(ymax/2),:int(xmax/2)])
    q2 = np.sum(grid[:int(ymax/2),int(xmax/2)+1:])
    q3 = np.sum(grid[int(ymax/2)+1:,:int(xmax/2)])
    q4 = np.sum(grid[int(ymax/2)+1:,int(xmax/2)+1:])
    return q1 * q2 * q3 * q4
 
print(getgrid(poses))   
final = [finalpos(p,v) for p,v in zip(poses,velos)]
print(getgrid(final))

print("The safety factor after %d seconds is %d" % (steps,safetyfactor(final)))

    