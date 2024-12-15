# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 22:18:00 2024

@author: Admin

Solution for the Advent of Code 2024 Challenge
Problem: Day 14

Task: Calculating positions ob objects in a wraparound 2D grid
"""

#from PIL import Image
import numpy as np
import networkx as nx
import re

xmax = 101#11 #101
ymax = 103#7 #103

#im = Image.open("mask.bmp")
#mask = np.array(im)[:,:,0]==255

with open('input.txt') as f:
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

#amt = len(poses)    

def nextpos(p,v):
    fc = p + v     
    fx = fc.real % xmax
    fy = fc.imag % ymax 
    return fx + fy*1j
 
def getgrid(poses):
    grid = np.zeros((ymax,xmax),dtype=int) 
    for p in poses:
        grid[int(p.imag)][int(p.real)] += 1
    return grid

#def detectmask(p,m):
#    return np.any(getgrid(p)*m)
 
#print(getgrid(poses))  
for i in range(int(1e6)): 
    poses = [nextpos(p,v) for p,v in zip(poses,velos)]
    g = getgrid(poses)
    if np.all(g<2):
        # i got lucky here, that this condition holds
        print(i+1)
        break
        # p = np.expand_dims(np.array(poses),1)
        # d = np.abs(p-p.T)
        # np.fill_diagonal(d,np.inf)
        # score = np.sum(np.min(d,axis=1))/amt
        # print('step=%d, score=%d',(i,score))
        # if score < 3:
        #     print(i)
        #     print(g)
        #     print()        




