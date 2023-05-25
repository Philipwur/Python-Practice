#%% 
# # Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order.

# double pointer method 
# -> if sum of right and left pointers are too large, move right pointer one left
# -> if sum of pointers are too small, move left pointer one right 
# -> doesnt work in leetcode because arrays are not sorted

class Solution:
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        Lp = 0
        Rp = len(nums) - 1
        nums.sort()
        
        while True:
            
            while Rp > Lp:
            
                sum = nums[Lp] + nums[Rp]
                print(Lp, Rp, sum)
                
                if sum > target:
                    Rp -= 1
                    
                elif sum < target: 
                    Lp += 1
                
                else:
                    return [Lp, Rp]
                

#hash table solution, scales worse because it doesnt make use of structure of data
# for some reason leetcode wants +1 on all numbers

class Solution2:
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
    
        seen = {}
        
        for i, value in enumerate(nums):
            
            if target - value in seen:
                return [seen[target - value] + 1, i + 1]
            
            seen[value] = i
                
                
                
#%%

nums = [2,7,11,15]
target = 9

test = Solution2().twoSum(nums, target)
        
print(test)
        
                
                
                
# First sort all numbers 
