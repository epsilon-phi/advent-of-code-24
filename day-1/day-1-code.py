# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:14:53 2024

@author: P. Czerwenka

Solution for the Advent of Code 2024 Challenge
Problem: Day 1
"""

"""
Part 1: Determining the sum of distances between two sorted lists
"""

import pandas as pd
import numpy as np

# load input data
data = pd.read_csv('input.txt',sep='   ',header=None,engine='python')

# sort both columns
col0 = np.sort(data[[0]].to_numpy(),0)
col1 = np.sort(data[[1]].to_numpy(),0)

# caluclate distances
dist = np.abs(col1 - col0)

# calculate sum
total_dist = np.sum(dist)
print("Total Distance: %d" % total_dist)

"""
Part 2: Determining the similarity score of the two lists
"""

# precalculate the unique elemnets and how often they appear
col0_unique,col0_ucount = np.unique(col0,return_counts=True)
col1_unique,col1_ucount = np.unique(col1,return_counts=True)

# throw away elemts which are only in one of the lists, as they do not 
# contribute to the similarity score 
col0_select = np.isin(col0_unique,col1_unique)
col1_select = np.isin(col1_unique,col0_unique)
col0_unique = col0_unique[col0_select]
col0_ucount = col0_ucount[col0_select]
col1_unique = col1_unique[col1_select]
col1_ucount = col1_ucount[col1_select]

# as the two lists now only contain unique values common to both lists (lists 
# are identical) we only have to multiply both occurances with the value itself
similarity = np.sum(col0_unique * col0_ucount * col1_ucount)
print("Similarity: %d" % similarity)