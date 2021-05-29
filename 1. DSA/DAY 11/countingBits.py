num = 5
rangeWalaArray = []
for i in range(num+1):
    rangeWalaArray.append(i)
solution = []
# print(rangeWalaArray)

# numToBinary ===|
print(bin(4))
for num in rangeWalaArray:
    count = 0
    for i in bin(num):
        if i=='1':
            count+=1
    solution.append(count)
print(solution)