#%%

#https://edabit.com/challenge/peezjw73G8BBGfHdW

def arithmetic_operation(n):
    
    values = n.split()
    
    op = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "//": lambda x, y: x / y
        }
    
    if (values[1] == "//") and (values[2] == "0"):
        return -1
    
    else:
        return op[values[1]](int(values[0]), int(values[2]))

#could also use a try-except scheme here (would be more versatile)

print(arithmetic_operation("12 + 12"))

print(arithmetic_operation("12 // 0"))