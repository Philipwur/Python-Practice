#Leetcode question 9
# Given An integer X, return true if xis a palindrome, false if otherwise


#matrix + list comprehension solution

class Solution:
    
    def isPalindrome(self, x: int) -> bool:
        
        string = str(x)
        leng = len(string)
            
        L = [string[x] for x in range(leng // 2)]
        R = [string[-x] for x in range(1, (leng // 2) + 1)]

        return L == R
    
    
# Solution in top 28% in runtime, bottom 36.7% in memory

#%%

# Solution without using Strings. Significantly worse preformance.
# Iteration 1

class Solution:
    
    def reverse_num(x: int) -> int: # function to reverse the number without str
    
        y = 0
        
        while x > 0:
            x, rem = divmod(x, 10)
            y = 10 * y + rem
            
        return y

    def isPalindrome(self, x: int) -> bool:

        if x != ((x ** 2) ** 0.5): # Filter out negatives
            return False
        
        # find length of number
        len = 1 
        while True:    
            if x // (10 ** len) == 0:
                break
            len += 1

        #correcting factor for odd len
        j = 0 
        if len % 2 == 1: 
            j = 1
        
        L = x // (10 ** ((len // 2) + j))
        R = x % (10 ** (len // 2))
        
        return R == Solution.reverse_num(L)

    
#%%

#Iteration 2 of no string solution

class Solution:
    
    def reverse_num(x: int) -> int: # function to reverse the number without str
    
        y = 0
        
        while x > 0:
            x, rem = divmod(x, 10)
            y = 10 * y + rem
            
        return y

    def isPalindrome(self, x: int) -> bool:
        
        if x > 0: # Filter out negatives
            return False
        
        return x == Solution.reverse_num(x)



#%%

print(divmod(154, 10))