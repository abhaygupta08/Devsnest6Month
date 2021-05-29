heap = "aabba"
needle = "bba"
m = len(heap)
n = len(needle)

def calHash(str):
	const = 10
	ans = 0
	p = 0
	for char in str:
		ans += (ord(char)-ord("a")+1)*const**p
		p+=1
	return(ans)
# ss = calHash(needle)
nhash = calHash(needle)
hhash = calHash(heap[:n])
# print(heap[:n])
# print(nhash)
# print()
# s = (nhash - (ord("a")-ord("a")+1))//10 + ((ord("e")-ord("a")+1)*10**(3))
# print(s)

for i in range(m-n):
	# print(heap[i])
	# print(heap[i:i+n])
	# hhash = calHash(heap[i:i+n])
	# print(hhash,nhash)
	
	if hhash==nhash:
		print(i)
		break
	
	else:
	# 	print(heap[i+n])
		hhash = (hhash - (ord(heap[i])-ord("a")+1))//10 + ((ord(heap[i+n])-ord("a")+1)*10**(n-1))
# print(heap[m-n:])
if heap[m-n:]==needle:
	print(m-n)