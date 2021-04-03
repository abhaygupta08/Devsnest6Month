n = '000000010100101'


count = 0
for i in str(bin(n)):
	if i=='1':
	count+=1
return count

