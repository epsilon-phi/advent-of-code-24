# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 22:54:12 2024

@author: Admin

Solution for the Advent of Code 2024 Challenge
Problem: Day 4

Task: Finding XMAS in a bunch of letters
"""

import re

with open('input.txt') as f:
    crossword = f.readlines()
     
# convert into list of list of chars    
c = [([char for char in line.replace("\n", "")]) for line in crossword]   

# rotate array of chars by 90 degrees
def rotate90(charmatrix):
    xsize = len(charmatrix[0]) # find size
    buffer = [(['' for char in line]) for line in charmatrix] # make empty copy       
    for y, line in enumerate(charmatrix):
        for x, elem in enumerate(line):
            # print(f'{x},{y}: {elem}')
            buffer[y][x] = charmatrix[x][(xsize-1)-y]
    return buffer

# rotate array of chars by 45 degrees, adding '.' in between, scaled to twice the size
def rotate45(charmatrix):
    xsize = len(charmatrix[0]) # find size
    ysize = len(charmatrix) # find size
    buffer = [(['.' for char in range(xsize*2-1)]) for line in range(ysize*2-1)] # make empty copy       
    for y, line in enumerate(charmatrix):
        for x, elem in enumerate(line):
            # print(f'{x},{y}: {elem}')
            buffer[(x+y)][(x-y)+xsize-1] = charmatrix[y][x]
    return buffer
        
# convert array of chars back into sting with linebreaks
def charmatrix2string(charmatrix):
    return ''.join([''.join(line)+'\n' for line in charmatrix])

total_xmas_count = 0
for _ in range(4):
    total_xmas_count = total_xmas_count + len(re.findall('XMAS', charmatrix2string(c)))
    cr = rotate45(c)
    total_xmas_count = total_xmas_count + len(re.findall('X.M.A.S', charmatrix2string(cr)))
    c = rotate90(c)

print("Number of 'XMAS'es %d" % total_xmas_count)

##########################################################################

total_mas_count = 0
# for y, line in enumerate(c[1:-1]):
#     for x, elem in enumerate(line[1:-1]):
#         if c[y+1][x+1] == 'A':
#             for i,j in [(i,j) for j in range(0,3,2) for i in range(0,3,2)]:
#                 if c[y+1][x+i] == 'M' and c[y+1][x+2-i] == 'S' and c[y+j][x+1] == 'M' and c[y+2-j][x+1] == 'S':
#                     total_mas_count += 1
        
cr = rotate45(c)

for y, line in enumerate(cr[2:-2]):
    for x, elem in enumerate(line[2:-2]):
        if cr[y+2][x+2] == 'A':
            for i,j in [(i,j) for j in range(0,5,4) for i in range(0,5,4)]:
                if cr[y+2][x+i] == 'M' and cr[y+2][x+4-i] == 'S' and cr[y+j][x+2] == 'M' and cr[y+4-j][x+2] == 'S':
                    total_mas_count += 1


print("Number of cross-'MAS'es %d" % total_mas_count)
























