def diagonal_sums(matrix):
    n = len(matrix)
    p_sum = 0
    s_sum = 0
    for i in range(n):
        p_sum += matrix[i][i]
        s_sum += matrix[i][n-i-1]
    return p_sum, s_sum, p_sum + s_sum

matrix = [
    [1, 2, 4],
    [6, 5, 6],
    [7, 8, 9]
]

p_sum, s_sum, total_sum = diagonal_sums(matrix)
total_sum-=matrix[1][1]
print("Sum of primary:", p_sum)
print("Sum of secondary:", s_sum)
print("Total sum of both diagonals:", total_sum)