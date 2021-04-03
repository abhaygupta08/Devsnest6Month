intervals = [[1,4],[4,5]]
solution = []
intervals.sort(key = lambda x: x[0])
current = intervals[0]
for i in range(1,len(intervals)):
    interval = intervals[i]
    if current[1]<interval[0]:
        solution.append(current)
        current = interval
    else:
        current[1] = max(current[1],interval[1])
        current[0] = min(current[0],interval[0])
solution.append(current)
print(solution)