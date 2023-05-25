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
                
#%%

nums = [3,2,4]
target = 6

test = Solution().twoSum(nums, target)
        
print(test)
        
                
                
                
# First sort all numbers 
