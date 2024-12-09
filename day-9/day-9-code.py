# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:17:05 2024

@author: Admin

Solution for the Advent of Code 2024 Challenge
Problem: Day 9

Task: Implement a defragmeting algorithm
"""

import numpy as np

with open('input.txt') as f:
    compactmap = list(f.read())

files = compactmap[::2]
frees = compactmap[1::2]

longmap = np.empty(0,dtype=str)
for idx,f in enumerate(files):
    longmap = np.append(longmap,np.full(int(f),str(idx)))
    if idx >= len(files)-1:
        break
    longmap = np.append(longmap,np.full(int(frees[idx]),'.'))
    
freepos = np.where(longmap=='.')[0]
sortmap = longmap.copy()    
print(sortmap)

def isdefragmented(l):
    empties = np.where(l=='.')[0]
    return np.all(np.diff(empties)==1)

replacepos = 0
for idx, relem in enumerate(reversed(longmap)):
    if relem == '.':
        continue
    if isdefragmented(sortmap):
        break
    sortmap[freepos[replacepos]] = relem
    sortmap[len(sortmap)-idx-1] = '.'
    replacepos += 1
    print(sortmap)
    
cleanmap = np.array([int(s) for s in sortmap[sortmap!='.']])
blockid = np.array([i for i in range(len(cleanmap))])

checksum = np.sum(np.int64(cleanmap * blockid))

print("Checksum after simple defragmentation %d" % checksum)




