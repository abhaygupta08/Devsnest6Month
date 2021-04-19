# DAY15 video

'''either in left subtree
or either in right subtree
or connectong both tree'''

def dia(node):
	if not node:
		return 0,0
	lp,lw = dia(root.left)
	rp,rw = dia(root.left)
	return 1+max(lp+rp) max(lw,rw,lp+rp+1)

class solution(object):
	return dia(root)+1