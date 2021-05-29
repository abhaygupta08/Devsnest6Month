matrix = [[1,2,3],[4,5,6],[7,8,9]]
n = len(matrix)
 
 ## swap around center row
for i in range(int(n/2)):
     for j in range(n):
         matrix[i][j],matrix[n-1-i][j] = matrix[n-1-i][j],matrix[i][j]

## swap around main diagonal left to right
for i in range(n):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        

for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=' ')
    print(' ')