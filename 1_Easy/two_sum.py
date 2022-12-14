#%%
"""
# https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            
            for j in range(i):
                
                if nums[i]+nums[j] == target:
                    return [i, j]    
                
#for large matrices it would be time efficient to add a function to get rid of 
#numbers larger than target