'''
height balanced BST
==> height or abs(leftSubstree - rightSubstree) <= 1

Approach -
 take middle elem then divide arr to 2 parts leftsubarr will be leftSubstree and same for right
 assign the middle of leftsubarry to left of root and same fir right middle elem
 go this untill subarr is empty if there is 1 elem left (we cant divide arr) then directly append it
'''
def arryToBST(arr):
	if not len(arr):
		return None
	mid = len(arr)//2
	return TreeNode(arr[mid],arryToBST(arr[:mid]),arryToBST(arr[mid+1:]))

print(arryToBST([1,2,3,4]).right.left.val)