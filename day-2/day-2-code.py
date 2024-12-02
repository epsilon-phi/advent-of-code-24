# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:00:44 2024

@author: P. Czerwenka

Solution for the Advent of Code 2024 Challenge
Problem: Day 2
"""

"""
Part 2: Determining the amount of 'safe' reports (lines)
"""

import numpy as np

safe_count = 0
safe_count_dampened = 0

# define a function to check if a report is safe
def check_report_safe(r):
    diff = np.diff(r) # caluclate distances
    if ( np.any(diff == 0) or  # unsafe, no change in value
        np.any(np.abs(diff) > 3) or  # unsafe, more or less than three
        np.any(np.sign(diff[0]) != np.sign(diff)) ): # unsafe, increasing and decreasing
        return False
    else:
        return True

# load input data
for line in open('input.txt'):
    elems_str = line.split()
    report = [int(x) for x in elems_str]
    
    # apply checking rules per report (line)
    if check_report_safe(report):
        safe_count = safe_count + 1
        safe_count_dampened = safe_count_dampened + 1
    else:
        # for each element in the report, remove the element and check again
        for idx,x in enumerate(report):
            new_report = report[0:idx] + report[idx+1:]
            if check_report_safe(new_report):
                safe_count_dampened = safe_count_dampened + 1
                break
            
    
print("Total Number of safe reports: %d" % safe_count)
print("Total Number of safe reports with dampening: %d" % safe_count_dampened)