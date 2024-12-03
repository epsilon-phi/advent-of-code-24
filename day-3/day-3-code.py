# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:49:15 2024

@author: P. Czerwenka

Solution for the Advent of Code 2024 Challenge
Problem: Day 3

Task: Exctracting correct instructions from corrupted instruction chain
"""

import re

# define a global state variable
state_count_muls = True

# load input data
# inst_chain = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
with open('input.txt') as f:
    inst_chain = f.read()

# multiply function used in the problem
def mul(a,b):
    global state_count_muls
    if state_count_muls:
        return  a * b
    else:
        return 0

def do():
    global state_count_muls
    state_count_muls = True
    return 0

def dont():
    global state_count_muls 
    state_count_muls = False
    return 0

# exctract instruction by regular expression
insts = re.findall("mul\(\d{1,3},\d{1,3}\)", inst_chain)

# evaluate the instructions by name
total_result = 0
for inst in insts:
    total_result = total_result + eval(inst)
    
print("Total Sum of mul() instructions: %d" % total_result)

# exctract extended instruction set by regular expression
insts = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", inst_chain)
insts = [s.replace("'", "") for s in insts]

# evaluate the instructions by name
total_result_ext = 0
for inst in insts:
    total_result_ext = total_result_ext + eval(inst)
    
print("Total Sum of mul() instructions with do() and don't()': %d" % total_result_ext)

