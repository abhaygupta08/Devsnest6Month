def check(root,x,y):
	if not root:
		return True
	
	return root.val>x and root.val<y and check(root.left,-1000000,root.val) and check(root.right,root.val,+100000000)

check(root,-(2<<31)+1,(2<<31)+1)