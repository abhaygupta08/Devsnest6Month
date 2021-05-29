solution = [[]]
for num in nums:
    solution += [[num] + x for x in solution]
print(solution)
