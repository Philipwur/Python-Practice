#%%

#https://edabit.com/challenge/3A3mHS5B3NNZddQL2

def interview(lst, tot):
    
    timelims = [5, 5, 10, 10, 15, 15, 20, 20]
    
    for i, j in zip(lst, timelims):
        
        if i > j:
            return "disqualified"
        
    if tot > 120 or len(lst) < 8:
        return "disqualified"
    
    return "qualified"
    

interview([5, 5, 10, 10, 15, 15, 20, 20], 130)

