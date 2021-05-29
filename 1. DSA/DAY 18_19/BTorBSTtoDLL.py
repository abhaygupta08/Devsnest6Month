def BTtoDLL(root):
	if not root:
		return None,None
	lh,lt = BTtoDLL(root.left)
	rh,rt = BTtoDLL(root.right)
	if lh:
		h = lh
		lt.right = root
		root.left = lt
	else:
		h = root
	if rt:
		t = rt
		rh.left = root
		root.right = rh
	else:
		t = root
	return h,t

'''
	      a         b         c 		d          e
	[None|1|b]   [a|3|c]   [b|7|d]   [c|9|e]   [d|12|None]
head													tail
'''