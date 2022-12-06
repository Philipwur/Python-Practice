#%%

#https://edabit.com/challenge/yvJbdkmKHvCNtcZy9

def is_disarium(n):
    
    x = "{}".format(n)
    y = 0
    
    for i in range(len(x)):
        y += int(x[i]) ** (i + 1)
    
    return n == y