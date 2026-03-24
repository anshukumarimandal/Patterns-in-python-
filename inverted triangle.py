#inverted triangle pattern 
n=int(input("Enter any number:"))
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()