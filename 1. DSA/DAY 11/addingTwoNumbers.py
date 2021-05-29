'''
#adding two numbers

disscuss : https://stackoverflow.com/questions/38557464/sum-of-two-integers-without-using-operator-in-python
'''
MAX_INT = 0x7FFFFFFF
MIN_INT = 0x80000000
MASK = 0x100000000
while b:
	a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)