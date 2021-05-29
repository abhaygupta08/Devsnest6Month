'''
Q - Given two strings s and t , return true if t is an anagram if s and false otherwise

ANAGRAM is a word or phrase formed by rearranging the letters of differnet word using all orignal letters only once
'''

s = 'ram'
t = 'mar'

'''
mar
mra
amr
arm
ram
rma
'''
hashmaps = {}
hashmapt = {}
for char in s:
	if not char in hashmaps:
		hashmaps[char] = 1
	else:
		hashmaps[char] += 1
for char in t:
	if not char in hashmapt:
		hashmapt[char] = 1
	else:
		hashmapt[char] += 1
print('s',hashmaps)
print('t',hashmapt)
print(hashmaps==hashmapt)



'''
METHOD 2

sort both arr and check if they are equal