

nums = [0,1,2]
'''
APPOACH 1

n = len(nums)
        nums.sort()
        for i in range(0,n):
            if nums[i]!=i:
                return i
        return i+1
'''


# APPOACH 2

n = len(nums)
return (n*(n-1))/2 - sum(nums)



# APPROACH 3
# best 

property of xor ^ ---- if a ^ b ==> 1 if a!+b else a==b
equal values pe xor karoge to 0 dega

x = len(nums)                           ## qki len(nums) reh jaega rangeExclusive hone ki wajah se
for i in range(len(nums)):
	x = x^nums[i]                      ##if nums[i] is equals i then value of x retains
	x = x^i
return x
