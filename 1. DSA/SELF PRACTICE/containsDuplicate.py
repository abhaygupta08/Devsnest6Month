nums = [1,2,3,1]
'''
nums.sort()
found = 0
for i in range(len(nums)):
	if nums[i]==nums[i-1]:
		found = 1
		break
print(found)
'''

'''
unique elem only dict
'''

'''
hshmap
'''
h = set()
found = False
for num in nums:
	if num in h:
		found = True
		break
	else:
		h.add(num)
print(found)