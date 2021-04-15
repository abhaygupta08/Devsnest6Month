n1 = [1,2,3,4,5,6,13]
n2 = [1,2,5,8,9]

newList = []

i,j = 0,0

while i < len(n1) and j < len(n2):
	if n1[i] < n2[j]:
		newList.append(n1[i])
		i+=1
	elif n1[i] > n2[j]:
		newList.append(n2[j])
		j+=1
	elif n1[i] == n2[j]:
		newList.append(n1[i])
		newList.append(n2[j])
		i+=1
		j+=1
if i == len(n1):
	while j < len(n2):
		newList.append(n2[j])
		j+=1
if j == len(n2):
	while i <len(n1):
		newList.append(n1[i])
		i+=1
print(newList)