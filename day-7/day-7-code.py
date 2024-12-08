# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 20:11:13 2024

@author: Admin

Solution for the Advent of Code 2024 Challenge
Problem: Day 7

Task: Determining correct operator usage in mathematical euqations
"""

import numpy as np
from itertools import product

with open('input.txt') as f:
    eqns = f.read().split('\n')
    
res = [int(eq.split(':')[0]) for eq in eqns]
numsets = [list(map(int, eq.split(': ')[1].split(' '))) for eq in eqns]
oplist = ['+', '*', '|']

total_result = 0 
for ridx, nset in enumerate(numsets):
    # generate all possible combinations of operators
    opcombs = list(product(oplist, repeat=len(nset)-1))
    for opcomb in opcombs:
        # calculate the result of this operator combination
        thisresult = nset[0]
        for opidx, op in enumerate(opcomb):
            if op == '+':
                thisresult += nset[opidx+1]
            elif op== '*':
                thisresult *= nset[opidx+1]
            # uncomment following 2 lines for part 1
            elif op == '|':
                thisresult = int(str(thisresult) + str(nset[opidx+1]))
            # check if we can exit early because the reuslt is over 
            if thisresult > res[ridx]:
                break
        # once finished, check if the result was achieved
        if thisresult == res[ridx]:
            total_result += thisresult
            break
        
print("Sum of achieveable results %d" % total_result)
  