# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 14:45:42 2024

@author: Admin

Solution for the Advent of Code 2024 Challenge
Problem: Day 11

Task: Number of Elements after applying modification rules
"""

import math
import numpy as np
import networkx as nx

with open('input.txt') as f:
    inputtext = f.read().split(' ')
    
# the rules sound like recursion, as they only ever apply to a single element
def apply_rules(elem):
    if elem == 0:
        return [1] # always return list
    digits = math.ceil(math.log10(elem+1))
    if digits % 2 == 0:
        # even number, part the number
        thisnum = list(str(elem))
        n1 = int(''.join(thisnum[:int(digits/2)]))
        n2 = int(''.join(thisnum[int(digits/2):]))
        return [n1, n2]
    # in all other cases, multiply
    return [elem * 2024]
        
def recursion_kernel(l,iter_left):
    # for every step in the recursion apply the rules and decrease iterations
    if iter_left == 0:
        return l
    if len(l) == 1:
        return recursion_kernel(apply_rules(l[0]),iter_left-1)
    else:
        e1 = recursion_kernel(apply_rules(l[0]),iter_left-1)
        e2 = recursion_kernel(apply_rules(l[1]),iter_left-1)
        return e1 + e2
    
# actual problem to solve
stones = [int(s) for s in inputtext]
# final_stones = [recursion_kernel([elem],25) for elem in stones]
print('Initial arrangement:')
print(stones)
for i in range(1,76):
    print('Calculating iteration %d' % i)
    new_stones = []
    for s in stones:
        new_stones += apply_rules(s)
    stones = new_stones
    #print('After %d iterations:' % i)
    #print(stones)
    print("current number of stones %d" % len(stones))
    print()

print("The total number of stones after 25 iterations is %d" % len(stones))