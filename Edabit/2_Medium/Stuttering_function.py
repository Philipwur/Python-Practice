#%%
#https://edabit.com/challenge/gt9LLufDCMHKMioh2

def stutter(word):
    
    repeat = word[0:2]
    
    return "{0}... {0}... {1}?".format(repeat, word)

print(stutter("pog"))

