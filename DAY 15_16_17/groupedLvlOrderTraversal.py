def height(node):
	if node is None:
		return 0
	else:
		# Compute the height of each subtree
		lheight = height(node.left)
		rheight = height(node.right)
		#Use the larger one
		if lheight > rheight :
			return lheight+1
		else:
			return rheight+1
def getLvlOrderRet(root):
	sol = []
	if not root:
		return []
	for i in range(1,height(root)+1):
		sol.append(printGivenLevel(root,i))
	return sol
def printGivenLevel(root , level):
	if not root:
		return []
	if root:
		if level == 1:
			return [root.data]
		else:
			return (printGivenLevel(root.left , level-1) + printGivenLevel(root.right , level-1)) 


# qq = getLvlOrderRet(x)
# print(qq)



##APPROACH 2
'''
step1 root X root wale elem daalo if pop(0) is X toh X ko appendkro mtlb 1 lvl done
step2 X ab ==> ab X 
step3 a aur b ke daalo ==> X cd ef  ==> cd ed X  lvl 2 done
...
...
'''
def groupedLvlOrder(root):
	if not root:
		return []
	q = [root,'X']
	ans = [[]]
	while True:
		node = q.pop(0)
		if node=='X':
			if len(q)==0:
				return ans
			q.append('X')
			ans.append([])
		else:
			ans[-1].append(node.data)
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)