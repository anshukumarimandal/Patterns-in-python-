n = int(input("Enter the number:"))
matrix = [[" " for _ in range(n)] for _ in range(n)]

top, bottom = 0, n - 1
left, right = 0, n - 1

while top <= bottom and left <= right:

    # Top row
    for i in range(left, right + 1):
        matrix[top][i] = "*"
    top += 2   # skip one row for hollow effect

    # Right column
    for i in range(top - 1, bottom + 1):
        matrix[i][right] = "*"
    right -= 2

    # Bottom row
    if top <= bottom:
        for i in range(right + 1, left - 1, -1):
            matrix[bottom][i] = "*"
        bottom -= 2

    # Left column
    if left <= right:
        for i in range(bottom + 1, top - 1, -1):
            matrix[i][left] = "*"
        left += 2

# Print pattern
for row in matrix:
    print(" ".join(row))