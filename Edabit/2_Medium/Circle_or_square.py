#%%

#https://edabit.com/challenge/4me7LifXBwj5rhL4n

def circle_or_square(rad, area):
    
    circ = 2 * 3.14 * rad
    perim = 4 * (area) ** 0.5
    
    return circ > perim

print(circle_or_square(5, 100))

