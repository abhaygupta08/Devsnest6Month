nums = [16, 17, 4, 3, 5, 2]
for i in range(len(nums)):
    leader = 1
    for j in range(i+1,len(nums)):
        if nums[i]>nums[j]:
            continue
        else:
            leader = 0
            break
    if leader:
        print(nums[i])

'''

MAX FROM RIGHT

'''
