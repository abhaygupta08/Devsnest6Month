
def presentRetHead(root,value):
	if not root:
		return None
	if root.data == value:
		return root
	return presentRetHead(root.left,value) or presentRetHead(root.right,value)
def getSubtree(root):
	if not root:
		return []
	return getSubtree(root.left) + [root.data] + getSubtree(root.right)

def getDescendents(root,headVal):
	if not root:
		return []
	head = presentRetHead(root,headVal)
	if head:
		return getSubtree(head)

print(getDescendents(x,3)) ##will return subtree inclusive of that target node

'''
remove targeted node data
'''
a = getDescendents(x,4)
a.remove(4)
print(a)