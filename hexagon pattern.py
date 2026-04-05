n = int(input("Enter size:"))# size of the hexagon

# Upper part
for i in range(n):
    print(" " * (n - i), end="")          # spaces
    print("* " * (n + i))                # stars

# Lower part
for i in range(n - 2, -1, -1):
    print(" " * (n - i), end="")         # spaces
    print("* " * (n + i))                # stars