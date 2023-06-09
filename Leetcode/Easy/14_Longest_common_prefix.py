# write a function that finds the longest common prefix

#%%

class Solution:
    
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        #prefix = sorted(strs, key = len())
        
        strmax = max(strs)
        strmin = min(strs)
        
        prefix = []
        
        for i in range(len(strmin)):
            
            if strmax[i] == strmin[i]:
                prefix.append(strmax[i])
            
            else:
                break
            
        return ''.join(prefix)
            
#%%

class Solution:
    
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        strs = sorted(strs)
        min = strs[0]
        max = strs[-1]
        
        prefix = ""
        
        for i in range(len(min)):
            
            if (min[i] != max[i]):
                return prefix
            
            prefix += min[i]
            
        return prefix

#%%

example = ["flower","flow","flight"]

example1 = [""]

exampleclass = Solution()

print(exampleclass.longestCommonPrefix(strs = example))