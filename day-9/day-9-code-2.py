# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 18:34:03 2024

@author: Admin

Solution for the Advent of Code 2024 Challenge
Problem: Day 9

Task: Part 2, Implement a file-wise defragmeting algorithm
"""

# WORK IN PROGRESS, although i dont know if i can manage

import numpy as np

with open('test.txt') as f:
    compactmap = list(f.read())

files = np.array([int(i) for i in compactmap[::2]]) # these now stay constant
frees = np.array([int(i) for i in compactmap[1::2]])

# search for first block longer than last element

# for idx, rfile in enumerate(reversed(files)):
#     freespaces = np.where(frees >= rfile)[0]
#     if freespaces.size != 0:
#         first_free = freespaces[0]
#         # put rfile into space at first_free
#         frees = [frees[:first_free] + [0] + frees[first_free:]]
#         files = [files[:first_free] + [0] + files[first_free:]]
        


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
this_file_len = 1
for idx, relem in enumerate(reversed(longmap)):
    if relem == longmap[idx-1]:
        this_file_len += 1
        continue
    #if isdefragmented(sortmap):
    #    break
    for lidx, lelem in enumerate(longmap):
        
    sortmap[freepos[replacepos]] = relem
    sortmap[len(sortmap)-idx-1] = '.'
    replacepos += 1
    print(sortmap)
    
cleanmap = np.array([int(s) for s in sortmap[sortmap!='.']])
blockid = np.array([i for i in range(len(cleanmap))])

checksum = np.sum(np.int64(cleanmap * blockid))

print("Checksum after simple defragmentation %d" % checksum)


