# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 16:34:43 2024

@author: Admin

Solution for the Advent of Code 2024 Challenge
Problem: Day 15

Task: Making moves and moving objects in a 2D grid
"""

import numpy as np

with open('input.txt') as f:
    inputtext = f.read()
    
grid,moves = tuple(inputtext.split('\n\n'))
grid = np.array([list(l) for l in grid.split('\n')],dtype=str)
moves = list(moves.replace('\n', ''))

unit_vector = {'>':np.array([1,0]),
               'v':np.array([0,1]),
               '<':np.array([-1,0]),
               '^':np.array([0,-1])}

def checkFree(pos,uv): # uv is the unit vector of direction (x,y)
    if grid[pos[1]+uv[1]][pos[0]+uv[0]] == '.':
        return True
    else:
        return False
    
def checkMovable(pos,uv): # uv is the unit vector of direction (x,y)
    if grid[pos[1]+uv[1]][pos[0]+uv[0]] == 'O':
        return True
    else:
        return False

def checkObstacle(pos,uv):
    #if pos[0] in [0,grid.shape[1]] or pos[1] in [0,grid.shape[0]] or grid[pos[1]][pos[0]] == '#':
    if grid[pos[1]+uv[1]][pos[0]+uv[0]] == '#':
        return True
    else:
        return False
    
def getFurthestFree(pos,uv):
    checkpos = pos.copy()
    while True:
        if checkFree(checkpos,uv):
            return checkpos + uv
        elif checkObstacle(checkpos,uv):
            return np.empty(0)
        checkpos += uv

def getCurrentPos():
    y,x = np.where(grid=='@')
    return np.array([x[0],y[0]])

def scoreResult():
    y,x = np.where(grid=='O')
    return np.sum(100*y+x)

# Main Program ------------------------------------------------------

print(grid)
for m in moves:
    direct = unit_vector[m]
    p = getCurrentPos()
    if checkFree(p,direct): # perform a move
        grid[p[1]+direct[1]][p[0]+direct[0]] = '@'
        grid[p[1]][p[0]] = '.'
    #elif checkObstacle(p,direct): # do nothing
    #    continue
    else: 
        far = getFurthestFree(p, direct)
        if far.size > 0: # found a point
            grid[p[1]+direct[1]][p[0]+direct[0]] = '@'
            grid[far[1]][far[0]] = 'O'
            grid[p[1]][p[0]] = '.'
        #else: # no move possible
        #    continue
    print('move: %s' % m)
    print(grid)
    print()
        
print("The sum of the final coordinates is %d" % scoreResult()) 
    