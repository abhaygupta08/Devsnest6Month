
##return bool
def searchInBST(root,data):
	if not root:  ##not found got to last elem
		return False
	if root.val == data:
		return True
	return searchInBST(root.left,data) if root.val > data else searchInBST(root.right,data)


## return pointer
def searchInBST(root,data):
	if not root:  ##not found got to last elem
		return None
	if root.val == data:
		return root
	return searchInBST(root.left,data) if root.val > data else searchInBST(root.right,data)
