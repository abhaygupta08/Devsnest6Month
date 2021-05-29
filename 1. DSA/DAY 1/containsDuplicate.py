'''
Q - Given an integer array nums return true if any value appears atleat twice in array else return false
'''
nums = [1,2,3,1]

numMap = dict()
for num in nums:
	if num in numMap:
		# print(num,'already')
		numMap[num] += 1
	else:
		numMap[num] = 1

for num in numMap:
	if numMap[num] > 1:   #atleast twice
		found = 'true'
		break
	else:
		found = 'false'
print(found)