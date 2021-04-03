'''
Q - Given an array of integers nums and a integer target return indicies of 2 numbers such as they add up to target
'''

nums = [2,7,11,6,15,3]
target = 9

for i in range(len(nums)):
	for j in range(i+1,len(nums)):
		# print('i:',i,'j:',j)		
		if nums[i]+nums[j] == target:
			print('['+str(i)+','+str(j)+']')

#---or
'''
nummap = {}
for i in range(len(nums)):
	number = nums[i]
	if target-number in nummap:
		print(nummap[target-number],i)
	nummap[number] = i
print(nummap)
'''