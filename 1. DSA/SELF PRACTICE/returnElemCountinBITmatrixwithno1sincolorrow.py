def chForSol(m,i,j):
    for r in range(len(matrix)):
        if m[r][j]==1 and r!=i:
            return 0
    for c in range(len(matrix[0])):
        if m[i][c]==1 and c!=j:
            return 0
    return 1

matrix = [
    [1,0,0,0,0],
    [0,1,1,0,0],
    [0,0,1,0,0],
    [0,0,0,0,0],
    [0,1,0,1,0]
    ]
res = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]==1:
            res += chForSol(matrix,i,j)
print(res)