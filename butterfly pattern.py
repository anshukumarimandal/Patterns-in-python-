n = 5  # size of the butterfly

# Upper part
for i in range(1, n + 1):
    # Left wing
    for j in range(1, i + 1):
        print("*", end="")
    
    # Spaces
    for j in range(1, 2 * (n - i) + 1):
        print(" ", end="")
    
    # Right wing
    for j in range(1, i + 1):
        print("*", end="")
    
    print()

# Lower part
for i in range(n, 0, -1):
    # Left wing
    for j in range(1, i + 1):
        print("*", end="")
    
    # Spaces
    for j in range(1, 2 * (n - i) + 1):
        print(" ", end="")
    
    # Right wing
    for j in range(1, i + 1):
        print("*", end="")
    
    print()