# Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise. \


### learing info -- 2 matrix means off --- > matrix[0][1] this will acess the 1 first row and second columns --> i is row j is columns 

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# main = []

# Original matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][1])

# Transpose: swap rows and columns
n = len(matrix)

for i in range(n):
    for j in range(i+1, n):  # only upper triangle to avoid double swapping
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    matrix[0].reverse()

print(matrix)

