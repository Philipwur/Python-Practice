#%% first try

class Solution:
    
    def romanToInt(self, s: str) -> int:
        
        roms = {'I' : 1, 
                'V' : 5,
                'X' : 10, 
                'L' : 50,
                'C' : 100,
                'D' : 500,
                'M' : 1000,
                }
        
        ints = 0
        p2 = 0
        
        for x in s[::-1]:
            
            p1 = roms[x]
    
            if p2 > p1:
                ints -= p1
                
            else:    
                ints += p1
            
            p2 = roms[x]
        
        return ints
            

#%% test

sol = Solution()

sol.romanToInt(s = "MCMXCIV")