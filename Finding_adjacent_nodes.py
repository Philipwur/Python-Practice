#%%

graph_1 = [
  [ 0, 1, 0, 1, 1 ],
  [ 1, 0, 1, 0, 0 ],
  [ 0, 1, 0, 1, 0 ],
  [ 1, 0, 1, 0, 1 ],
  [ 1, 0, 0, 1, 0 ]
]

graph_2 = [
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
]

def is_adjacent(matrix, node1, node2):
    
    output = False
    
    if matrix[node1][node2] == 1:
        output = True
     
    return output

print(is_adjacent(graph_1, 3, 2))

