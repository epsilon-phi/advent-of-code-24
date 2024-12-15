# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 16:34:43 2024

@author: Admin

Solution for the Advent of Code 2024 Challenge
Problem: Day 15

Task: Making moves and moving objects in a 2D grid - for part 2
"""

import numpy as np

with open('input.txt') as f:
    inputtext = f.read()

replacement = {'#': '##',
               'O': '[]',
               '.': '..',
               '@': '@.'}

grid,moves = tuple(inputtext.split('\n\n'))
for r in replacement:
    grid = grid.replace(r, replacement[r])
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
    
def checkObstacle(pos,uv): # uv is the unit vector of direction (x,y)
    if grid[pos[1]+uv[1]][pos[0]+uv[0]] == '#':
        return True
    else:
        return False

def checkMovable(pos,uv):
    #if pos[0] in [0,grid.shape[1]] or pos[1] in [0,grid.shape[0]] or grid[pos[1]][pos[0]] == '#':
    if grid[pos[1]+uv[1]][pos[0]+uv[0]] in ['[',']']:
        return True
    else:
        return False
    
def moveFurthestHorizFree(pos,uv):
    checkpos = pos.copy()
    if checkFree(checkpos,uv):
        grid[checkpos[1]+uv[1]][checkpos[0]+uv[0]] = grid[checkpos[1]][checkpos[0]]
        return True
    elif checkObstacle(checkpos,uv):
        return False
    if moveFurthestHorizFree(checkpos + uv,uv): # successful on deeper level
        grid[checkpos[1]+uv[1]][checkpos[0]+uv[0]] = grid[checkpos[1]][checkpos[0]]
        return True
    else:
        return False
     
def moveFurthestVerticalFree(pos,uv):
    checkposes = []
    for p in pos:
        if grid[p[1]][p[0]] == '[':
            checkposes.append(p)
            checkposes.append(p + unit_vector['>']) 
        elif grid[p[1]][p[0]] == ']':
            checkposes.append(p)
            checkposes.append(p + unit_vector['<']) 
        else:
            print('something went very wrong')
            return False
    seen = set()
    checkposes = [cp for cp in checkposes if repr(cp) not in seen and (seen.add(repr(cp)) or True)]
    
    nextposes = [] # determine if serach concludes, must go deeper or terminates
    for cp in checkposes:
        if checkObstacle(cp,uv):
            return False
        elif checkMovable(cp,uv):
            nextposes.append(cp)
    
    result = True
    if len(nextposes) > 0: # serach must go deeper
        nextposes = [nxp + uv for nxp in nextposes]
        result = moveFurthestVerticalFree(nextposes,uv)
        
    if result == False:
        return False
    else: # search was successful and everything is free so move 
        for cp in checkposes:
            grid[cp[1]+uv[1]][cp[0]+uv[0]] = grid[cp[1]][cp[0]]
            grid[cp[1]][cp[0]] = '.'
        return True

def pushObstacles(pos,uv):
    if np.all(uv == unit_vector['>']) or np.all(uv == unit_vector['<']): # vertical movement, as in first part
        return moveFurthestHorizFree(pos,uv)
    else: # a lot harder 
        return moveFurthestVerticalFree([pos],uv)

def getCurrentPos():
    y,x = np.where(grid=='@')
    return np.array([x[0],y[0]])

def scoreResult():
    y,x = np.where(grid=='[')
    return np.sum(100*y+x)

def moveActor(pos,uv):
    grid[p[1]+direct[1]][p[0]+direct[0]] = '@'
    grid[p[1]][p[0]] = '.'

def charmatrix2string(charmatrix):
    return ''.join([''.join(line)+'\n' for line in charmatrix])

# Main Program ------------------------------------------------------

print(charmatrix2string(grid))
for m in moves:
    direct = unit_vector[m]
    print('move: %s' % m)
    p = getCurrentPos()
    if checkFree(p,direct): # perform a move
        moveActor(p,direct)
    elif checkMovable(p,direct):
        if pushObstacles(p+direct, direct): # if could move boxes
            moveActor(p,direct)

    print(charmatrix2string(grid))
    print()
        
print("The sum of the final coordinates is %d" % scoreResult()) 
    