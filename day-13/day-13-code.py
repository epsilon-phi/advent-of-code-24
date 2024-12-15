# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 00:38:22 2024

@author: Admin
"""

import numpy as np
import re

# a = 94+34j # cost 3
# b = 22+67j # cost 1
# p = 8400+5400j

a = 26+66j # cost 3
b = 67+21j # cost 1
p = 12748+12176j

with open('input.txt') as f:
    inputtext = f.read()
    inputtext = re.sub('[^\d,\n]','',inputtext)
    inputtext = inputtext.split('\n\n')

inputtext = [this.replace(',','+') for this in inputtext] 
inputtext = [this.split('\n') for this in inputtext]
inputnums = [[complex(el+'j') for el in this] for this in inputtext]


# its quasi pascals triangle and 
# the cost is the same for any path to a node

def LinearCombCoeff(level):
    return np.array([(level-i,i) for i in range(level+1)])

def LinearComb(a,b,level):
    return np.array([a*ca+b*cb for ca,cb in LinearCombCoeff(level)])

def MaxSearchDepth(a,b,p):
    return np.max([np.ceil(p.real/a.real),np.ceil(p.imag/a.imag),np.ceil(p.real/b.real),np.ceil(p.imag/b.imag)])

def ComponentsExceeded(t,c):
    return np.bitwise_or(t.imag > c.imag,t.real > c.real)
  
def LinearCombSearch(a,b,p): # lower cost goes first for correct cost caluclation 
    smax = int(MaxSearchDepth(a,b,p))
    #smax = 100
    lowest_cost = np.inf
    for l in range(2,smax+1):
        this = LinearComb(a,b,l) 
        for goal in np.where(this==p):
            if goal.size > 0:
                cb,ca = LinearCombCoeff(l)[goal[0]]
                cost = l+goal[0]*2
                print('  Solution at %dxA,%dxB with cost %d' % (ca,cb,cost))
                if cost < lowest_cost:
                    lowest_cost = cost
        if np.all(ComponentsExceeded(this,p)):
            break
    if lowest_cost == np.inf:
        print('  No Solution')
    return lowest_cost
  
total_cost = 0    
possible_wins = 0  
for machine in inputnums:
    btna = machine[0]
    btnb = machine[1]
    prize = machine[2]
    print('Analyzing machine with A=%s B=%s and Prize %s' % (btna,btnb,prize))
    this_cost = LinearCombSearch(btnb,btna,prize)
    if this_cost!= np.inf:
        possible_wins += 1
        total_cost += this_cost
   
    
print("In total %d prizes can be won for %d tokens" % (possible_wins,total_cost))
    
# for the second part i would need to solve a system of diopantine equations
# and i have found no good solvers for that....
    
    
    
    
    
    
    
    
    
    
    
