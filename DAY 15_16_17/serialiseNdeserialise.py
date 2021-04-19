

## list <==> tree
'''
letsay tree is 
		1
	  2   3
    4    5 6
===> X reprensts null
list like = root(leftSubstree),(RightSubtree)
list = 1(2(4),(X)),(3(5),(6))
'''

def serialise(root):
	if not root:
		return 'X'
	return str(root.val) + '(' +self.serialise(root.left) +'),(' + self.serialise(root.right)+')'

def deserialise(data):
	if data=='X':
		return None
	data = data.split('(',1)  #here 1 restricts the first encountered opening bracket
	n = TreeNode(int(data[0])) ##root node
	data = '(' + data[1] ##left + right Substree
	i,count=0,0
	for i in range(len(data)):
		c = data[i]
		if c=='(':
			count +=1
		elif c==')':
			count-=1
			if count==0:
				n.left = self.deserialise(data[1:i])
				n.right = self.deserialise(data[i+3:-1])  ##  ),(
				return n