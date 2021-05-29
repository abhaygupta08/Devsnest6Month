intervals = [[1,2],[2,3],[3,4],[1,3]]
N,count = len(intervals),0
if N < 1:
    exit()
intervals.sort(key = lambda a:a[0])
for i in range(1,N):
    if intervals[i][0]<intervals[i-1][1]:
        intervals[i][1] = min(intervals[i-1][1],intervals[i][1])
        count+=1
print(count)