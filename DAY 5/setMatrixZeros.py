matrix = [[1,1,1],[1,0,1],[1,1,1]]
row = len(matrix)
if row:
    coloumn = len(matrix[0])
# i 1 j 1
# 01 11 21 | 10 11 12

toDeletei = []
toDeletej = []

for i in range(row):
    for j in range(coloumn):
        if matrix[i][j]==0:
            toDeletei.append(i)
            toDeletej.append(j)
print(toDeletej)
print(toDeletei)
for i in toDeletei:
    for j in range(coloumn):
        matrix[i][j]=0
for j in toDeletej:
    for i in range(row):
        matrix[i][j]=0

for i in range(row):
    for j in range(coloumn):
        print(matrix[i][j],end=' ')
    print(' ')
