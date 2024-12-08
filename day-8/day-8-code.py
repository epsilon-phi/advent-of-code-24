# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 21:26:44 2024

@author: Admin

Solution for the Advent of Code 2024 Challenge
Problem: Day 8

Task: Caluclating extendep positions in a 2d grid
"""

import numpy as np
from itertools import combinations

with open('input.txt') as f:
    rawfile = f.read()
    freq_list = np.unique(list(rawfile.replace("\n", "").replace(".", "")))
    freq_list = [str(f) for f in freq_list]
    full_grid = np.array([list(l) for l in rawfile.split()])

class Ground:
    def __init__(self, grid, freqs):
        self.antennas = {}
        for idx, f in enumerate(freqs):
            self.antennas[f] = (grid==f)
        self.freqs = freqs
        y,x = grid.shape
        self.xmax = x
        self.ymax = y
        self.inferference = np.full_like(grid,False,dtype=bool)
        for f in self.freqs:
            #self.inferference += self.find_interferences(f)  
            self.inferference += self.find_interferences_advanced(f)
    def draw(self):
        def draw_npchararray(b):
            b = np.array2string(b).replace("'", "")
            b = b.replace("'", "").replace("[[", " [").replace("]]", "] ")
            print(b)
        buffer = np.full((self.ymax,self.xmax),'.',dtype=str)
        for f in self.freqs:
            buffer[self.antennas[f]] = f
        draw_npchararray(buffer)
        print('-------')
        buffer = np.full((self.ymax,self.xmax),'.',dtype=str)
        buffer[self.inferference] = '#'
        for f in self.freqs:
            buffer[self.antennas[f]] = f
        draw_npchararray(buffer)
        print('-------')
        buffer = np.full((self.ymax,self.xmax),'.',dtype=str)
        buffer[self.inferference] = '#'
        draw_npchararray(buffer)
    def find_interferences(self,freq): # interference find algorithm for part 1
        apts = self.find_coordinates(freq)
        antenna_pairs = list(combinations(apts, 2))
        buffer = np.full((self.ymax,self.xmax),False,dtype=bool)
        for p1,p2 in antenna_pairs:
            i1 = 2*p1 - p2
            if np.all(i1 >= 0) and np.all(i1 < np.array([self.xmax,self.ymax])):
                buffer[i1[1]][i1[0]] = True
            i2 = 2*p2 - p1
            if np.all(i2 >= 0) and np.all(i2 < np.array([self.xmax,self.ymax])):
                buffer[i2[1]][i2[0]] = True
        return buffer
    def find_interferences_advanced(self,freq): # interference find algorithm for part 2
        apts = self.find_coordinates(freq)
        antenna_pairs = list(combinations(apts, 2))
        buffer = np.full((self.ymax,self.xmax),False,dtype=bool)
        for p1,p2 in antenna_pairs:
            d1 = p1 - p2
            i1 = p1.copy()
            while np.all(i1 >= 0) and np.all(i1 < np.array([self.xmax,self.ymax])):
                buffer[i1[1]][i1[0]] = True
                i1 += d1
            d2 = p2 - p1
            i2 = p2.copy()
            while np.all(i2 >= 0) and np.all(i2 < np.array([self.xmax,self.ymax])):
                buffer[i2[1]][i2[0]] = True
                i2 += d2
        return buffer
    def find_coordinates(self,freq):
        antennamap = self.antennas[freq]
        y, x = np.where(antennamap)
        pts = list(zip(x, y))
        pts = [np.array([x,y]) for x,y in pts] 
        return pts
    def interference_count(self):
        return np.sum(self.inferference)
        

this_problem = Ground(full_grid,freq_list)
this_problem.draw()

print("Number of interference positions %d" % this_problem.interference_count())






























