unDirGraph = [
[1,4],
[0,2],
[1,3,4],
[2,4],
[0,2,3]
]
v = [0]*(len(unDirGraph)-1)
def isCycleUtil(current):
	if v[current]:
		return True
	v[current] = True
	flag = False
	for i in unDirGraph[current]:
		flag = isCycleUtil(i)
		if flag:
			return True
	return False
def detectCycle(current):
	flag = False
	for i in range(len(unDirGraph)):
		v[i] =1
		for j in unDirGraph[i]:
			flag = isCycleUtil(j)
			if flag:
				return True
		v[i] = 0
	return False
print(detectCycle(0))