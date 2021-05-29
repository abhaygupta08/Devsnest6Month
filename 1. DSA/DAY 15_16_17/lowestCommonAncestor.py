
def lca(root,n1,n2):
	if root is None:
		return None
	if root.data == n1 or root.data == n2:
		return root.data
	left_lca = lca(root.left, n1, n2)
	right_lca = lca(root.right, n1, n2)
	if left_lca and right_lca:
		return root.data
	return left_lca if left_lca is not None else right_lca

##n1 and n2 are values
##if n1 is node then check in 2nd if statement if root==p or root==q and return root instead of root.data
print(lca(x,3,5))


##approcach 2
#//////////Not tested


def printAncestors(root, target,a=[]):
	if root == None:
		return []
	if root.data == target:
		return True
	if (printAncestors(root.left, target,a) or 
        printAncestors(root.right, target,a)):
		a.append(root.data)
		return a
	return False
a,b =[],[]
print(printAncestors(x,2,a))
print(printAncestors(x,1,b))
print(list(set(a) and set(b))[0])