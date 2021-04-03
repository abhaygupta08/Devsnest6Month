
'''
algo----
if all are negative then return most neg number

subarray + contigous(w/ atleat one member)
case 2 : start from 1st one if current sum is greater than max then max is curent elif sum of current is negative then max is 0 
'''
#if not with atleast one number we could return 0 when maxsum is negative
nums = [-2,1,-3,4,-1,2,1,-5,4]
currentSum = 0
MaxSum = 0
if max(nums) < 0:
	MaxSum = max(nums)
	print(MaxSum)
	exit()
for num in nums:
	currentSum +=num
	if currentSum > MaxSum:
		MaxSum = currentSum
	elif currentSum < 0:
		currentSum = 0
print(MaxSum)