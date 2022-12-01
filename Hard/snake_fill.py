#%%

#https://edabit.com/challenge/Y5Ji2HDnQTX7MxeHt

def snakefill(n):
    
    snake, i = 1, -1
    
    while snake <= (n ** 2):
        
        snake = snake * 2
        i += 1
        
    return i

print(snakefill(24))