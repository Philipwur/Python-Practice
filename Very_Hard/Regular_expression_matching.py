# %%

#https://edabit.com/challenge/XhyPkjEDQ3Mz5AFaH

#https://leetcode.com/problems/regular-expression-matching/


#UNSOLVED RN

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
# pattern has two active conditions, mem and pointer
# a * updates the memory function and pointer moves on to the next char
# if memory is used to validate char, nothing updates in terms of pointers
# if pointer is used to validate char, there is a check for * and previous cache 
# is removed

# j is pointer and cache is * point


# This version does not have a solution for when * means 0 of char
def is_match(s : str, p : str) -> bool:
    
    if not p:
        return not s
    
    j = 0
    
    for i in range(len(s)):
        
        #check for cache and updating of pattern pointer
        try:
            if p[j+1] == "*":
                if p[j] == s[i]:
                    
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


# we need some kind of checking for the len to avoid having to use try

#steps
# 1. is the p a *
#   y -> check if the p == s, .
#       y -> loop next s
#       n -> j + 2 and start from 1.
#           if j == len(p)
#               return false
#   n -> check if p == s, .
#       y -> loop next s, j+1
#       n -> return False
# return True