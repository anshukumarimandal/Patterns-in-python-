# Circle pattern using nested loops

radius = int(input("Enter radius:"))
for i in range(-radius, radius + 1):
    for j in range(-radius, radius + 1):
        if i*i + j*j <= radius*radius:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()