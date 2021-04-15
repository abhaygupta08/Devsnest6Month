matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
top,left = 0,0
right,bottom = len(matrix[0])-1,len(matrix)-1
solution = []

#direction for where to move from where
dir = 1
'''
1 - top left to top right
2 - top right to bottom right
3- bottom right to bottom left
4 - bottom left to top left
'''

# print(top,left,bottom,right)
# print(matrix)
while(top<=bottom and left<=right):
    if(dir==1):
        for i in range(left,right+1):
            solution.append(matrix[top][i])
        top+=1
        dir = 2
    elif dir==2:
        for i in range(top,bottom+1):
            solution.append(matrix[i][right])
        right-=1
        dir = 3
    elif dir==3:
        print(right,left-1)
        for i in range(left,right+1)[::-1]:
            solution.append(matrix[bottom][i])
        bottom-=1
        dir = 4
    elif dir==4:
        for i in range(top,bottom+1)[::-1]:
            solution.append(matrix[i][left])
        left+=1
        dir=1
print(solution)