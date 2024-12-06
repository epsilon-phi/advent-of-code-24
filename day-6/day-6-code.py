# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 09:07:34 2024

@author: Admin

Solution for the Advent of Code 2024 Challenge
Problem: Day 6

Task: Determining the path of an actor on a 2D-grid
"""

import numpy as np

with open('input.txt') as f:
    full_grid = np.array([list(l) for l in f.read().split()])
    
class Ground:
    def __init__(self, grid):
        self.map = np.logical_not(grid=='#')
        y,x = full_grid.shape
        self.xmax = x
        self.ymax = y
        self.visited = np.full_like(grid,False,dtype=bool)
        self.turnpos = np.full_like(grid,False,dtype=bool)
    def draw(self,a):
        buffer = np.full_like(self.map,'.',dtype=str)
        buffer[self.map==False] = '#'
        buffer[self.visited] = 'X'
        if (a.x,a.y) != (-1,-1):
            buffer[a.y][a.x] = a.dir
        buffer = np.array2string(buffer).replace("'", "")
        buffer = buffer.replace("'", "").replace("[[", " [").replace("]]", "] ")
        print(buffer)
        print()
    def visited_positions(self):
        return np.sum(self.visited * 1)

class Actor:
    def __init__(self, grid):
        self.dirs = ['<','^','>','v']
        y,x = [np.where(match==grid) for match in self.dirs if np.any(match == grid)][0]
        self.x = x[0]
        self.y = y[0]
        self.dir = [match for match in self.dirs if np.any(match == grid)][0]
    def move(self, grid):
        # perform update of visited 
        grid.visited[self.y][self.x] = True
        # check if out of bounds
        if (self.dir == '<' and self.x == 0) or \
            (self.dir == '^' and self.y == 0) or \
            (self.dir == '>' and self.x == grid.xmax-1) or \
            (self.dir == 'v' and self.y == grid.ymax-1):
            # finished
            self.x = -1 
            self.y = -1 
            return
        # check if actor needs to be rotated, perhaps multiple times
        rotated = False
        for i in range(4):
            if self.dir == '<' and grid.map[self.y][self.x-1] == False:
                self.dir = '^'
                rotated = True
            elif self.dir == '^' and grid.map[self.y-1][self.x] == False:
                self.dir = '>'
                rotated = True
            elif self.dir == '>' and grid.map[self.y][self.x+1] == False:
                self.dir = 'v'
                rotated = True
            elif self.dir == 'v' and grid.map[self.y+1][self.x] == False:
                self.dir = '<'
                rotated = True
            else:
                break
            # if rotated more than 4 times we are stuck in a loop
            if i == 3:
                self.x = -2 
                self.y = -2 
                return
        # check if we turned at this position before, then its a loop
        if rotated:
            if grid.turnpos[self.y][self.x]:
                # finished
                self.x = -2 
                self.y = -2 
                return
            else:
                grid.turnpos[self.y][self.x] = True
        # move actor
        if self.dir == '<':
            self.x = self.x-1
        elif self.dir == '^':
            self.y = self.y-1
        elif self.dir == '>':
            self.x = self.x+1
        elif self.dir == 'v':
            self.y = self.y+1 

actor = Actor(full_grid)
ground = Ground(full_grid)
ground.draw(actor)

while (actor.x,actor.y) != (-1,-1):
    actor.move(ground)
    #ground.draw(actor)

print("Number of uniquely visited positions %d" % ground.visited_positions())

# second task: find loops with one additional obstruction, by brute force testing all visitied positions

number_of_loops = 0
for y,x in np.argwhere(ground.visited):
    # place additional obstruction
    test_grid = full_grid.copy()
    # skip if we are at the position of the actor
    if test_grid[y][x] == '<' or test_grid[y][x] == '^' or test_grid[y][x] == '>' or test_grid[y][x] == 'v':
        continue
    test_grid[y][x] = '#'
    test_actor = Actor(test_grid)
    test_ground = Ground(test_grid)
    
    # run test
    run_test = True
    while run_test:
        test_actor.move(test_ground)
        #test_ground.draw(test_actor)
        if (test_actor.x,test_actor.y) == (-1,-1):
            run_test = False
            print(f"Testing obstruction at x{x},y{y}: escaped")
        elif (test_actor.x,test_actor.y) == (-2,-2): 
            run_test = False
            #test_ground.draw(test_actor)
            print(f"Testing obstruction at x{x},y{y}: stuck in loop")
            number_of_loops += 1
            
print("Number of obstruction positions resulting in loop %d" % number_of_loops)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    