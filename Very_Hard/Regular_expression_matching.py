# %%

#https://edabit.com/challenge/XhyPkjEDQ3Mz5AFaH

#https://leetcode.com/problems/regular-expression-matching/

"""
Given an input string s and a pattern p, 
implement regular expression matching with support for "." and "*" .

Examples

is_match("aa", "a") ➞ false
# "a" does not match the entire string "aa".

is_match("aa", "a*") ➞ true
# "*" means zero or more of the preceding element, "a".
# Therefore, by repeating "a" once, it becomes "aa".

is_match("ab", ".*") ➞ true
# ".*" means "zero or more (*) of any character (.)".

Notes

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

"""
# This version does not have a solution for when * means 0 of char
def is_match(s, p) -> bool:
    
    if not p:
        return not s
    
    cache = None
    j = 0
    
    for i in range(len(s)):
        
        #check for cache and updating of pattern pointer
        try:
            if p[j+1] == "*":
                cache = p[i]
                j += 2
                print("cache point found")
        except:
            continue
        
        #checking whether char can be solved with pointer
        if s[i] in (p[j], "."):
            j += 1
            cache = None
            print("solved with pointer")
            
        #checking whether char can be solved with cache
        if s[i] == cache:
            print("solved with cache")
        
        else: 
            return False
    
    return True

print(is_match("aaab", "a*bc"))

# pattern has two active conditions, mem and pointer
# a * updates the memory function and pointer moves on to the next char
# if memory is used to validate char, nothing updates in terms of pointers
# if pointer is used to validate char, there is a check for * and previous cache 
# is removed

# j is pointer and cache is * point