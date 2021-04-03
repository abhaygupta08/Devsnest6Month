'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer
'''

nums = [1,0,3,0,4]
zero_count,allMul,N = 0,1,len(nums)
product = []
for num in nums:
	if num == 0:
		zero_count+=1
	else:
		allMul *= num
if zero_count == 0:
	for i in range(N):
		product.append(int(allMul/nums[i]))
elif zero_count == 1:
	for i in range(N):
		if nums[i]==0:
			prod = allMul
		else:
			prod = 0
		product.append(prod)
elif zero_count > 1:
	for i in range(N):
		product.append(0)
print(product)