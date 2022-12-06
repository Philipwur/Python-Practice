#%%

#https://edabit.com/challenge/JzBLDzrcGCzDjkk5n

vowels = {
    "a" : "0",
    "e" : "1",
    "i" : "2",
    "o" : "2",
    "u" : "3"
}

def encrypt(word):
    
    word = list(word[::-1])
    
    for i in range(len(word)):
        
        if word[i] in vowels:
            
            word[i] = vowels[word[i]]
    
    return "".join(word) + "aca"