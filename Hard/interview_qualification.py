#%%

#https://edabit.com/challenge/3A3mHS5B3NNZddQL2

def interview(lst, tot):
    
    timelims = [5, 5, 10, 10, 15, 15, 20, 20]
    
    if tot > 120 or len(lst) < 8:
        return "disqualified"
    
    for i, j in zip(lst, timelims):
        
        if i > j:
            return "disqualified"
        
    return "qualified"
    

interview([5, 5, 10, 10, 15, 15, 20, 20], 130)


#%%

import matplotlib.pyplot as plt
import numpy as np

# Define the potential energy function
def potential_energy(coordinates):
  x, y, z = coordinates
  V = x**2 + y**2 + z**2
  return V

# Create a grid of coordinates
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Calculate the potential energy at each point on the grid
Z = potential_energy((X, Y, 0))

# Plot the potential energy surface
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.show()
