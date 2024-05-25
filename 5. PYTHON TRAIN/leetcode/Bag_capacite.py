"""Maximum Bags With Full Capacity of Rocks
You have n bags numbered from 0 to n-1. You are given two 0-indexed integer arrays capacity and rocks. The ith bag can hold a maximum of capacity[i] rocks and currently contains rocks[i] rocks. You are also given an integer additionalRocks, the number of additional rocks you can place in any of the bags.
Return the maximum number of bags that could have full capacity after placing the additional rocks in some bags.

The number of rocks in each bag are now [2,3,4,4] Bags 0, 1, and 2 have full capacity. There are 3 bags at full capacity, so we return 3. It can be shown that it is not possible to have more than 3
bags at full capacity. Note that there may be other ways of placing the rocks that result in an answer of 3.

Example 1:
Input: capacity = [2,3,4,5], rocks = [1,2,4,4), additional Rocks = 2
Output: 3
Explanation:
Place 1 rock in bag 0 and 1 rock in bag 1.

"""

import unittest

import test

def Solution(capacity: list[int], rocks : list[int], additionalRocks : int) -> int:
    needed_rocks  = []
    for i in range(len(capacity)):
        t = capacity[i] - rocks[i]
        needed_rocks.append(t)
        
    needed_rocks.sort()    
    
    full_bags = 0
    
    for rocket_needed in needed_rocks :
        if additionalRocks >= rocket_needed:
            additionalRocks -= rocket_needed
            full_bags += 1
        else:
            break
        
    return full_bags
    

import test
def runTest(Solution):
    capacity = [2, 3, 4, 5]
    rocks = [1, 2, 4, 4]
    additionalRocks = 2
    print(Solution(capacity, rocks, additionalRocks))  

runTest(Solution)