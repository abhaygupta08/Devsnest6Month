'''
             ==__property__==
[=] all leftSubstree elem has val less than root
[=] all rightSubstree elem has val greater than root

        A 
      B   C         where  B < A < C

### Inorder of BST is sorted Sequence
### all elements are unique
#			but if are same elements we can put in right subtree but there are complications


ADDITION
is to to done on leaf node

DELETION
1. if node is just before leaflvl and has 1 child only
                     Tree                          Tree
                        3           OR                 3
                          5                          5
then remove that node(in this case 3) and replace it with val 5

2. if node has 2 childs
		node ke left ke rightmost elem se replace
		   or
		node ke right ke leftmost elem se replace

'''





class TreeNode():
	def __init__(self,val=0,left=None,right=None):
		self.val = val
		self.left = left
		self.right = right

x = TreeNode(5,TreeNode(3,TreeNode(2),TreeNode(4)),TreeNode(7))
'''
     5
  3    7
2  4
'''

def searchInBST(root,data):
	if not root:  ##not found got to last elem
		return False
	if root.val == data:
		return True
	return searchInBST(root.left,data) if root.val > data else searchInBST(root.right,data)

### not SOLVED
def additionInBST(root,data):
	n = TreeNode(data)
	p = root
	if not root: ##if tree is empty
		return n
	while root.left.val < data < root.right.val:
		if not root:
			return
		if root.left.val > data:
			root = root.left
		elif root.right.val < data:
			root = root.right
	if root.left.val < data:
		root.left.right = n
	else:
		root.left.left = n
	return p 

'''
validate BST

Approach 1 
range method (exclusive)
-inf to +inf
root aaya range mei to Ok
left walo ki range -inf to root 
right walo ki range root to +inf
recursive
'''
def check(root,x,y):
	if not root:
		return True
	
	return root.val>x and root.val<y and check(root.left,-1000000,root.val) and check(root.right,root.val,+100000000)

# def validBST(root):
# 	return
	
def getMin(root):
	while root.left:
		root = root.left
	return root


def sumOfBST(root):
	if not root:
		return 0
	return sumOfBST(root.left) + root.val + sumOfBST(root.right)


def inOrder(root):
	if not root:
		return []
	return inOrder(root.left) + [root.val] + inOrder(root.right)


aa = inOrder(x)
def greaterSumBST(root,aa):
	if not root:
		return None
	root.val = sum(aa[aa.index(root.val):])
	greaterSumBST(root.left,aa)
	greaterSumBST(root.right,aa)
	return root

def find(root,value):
    if not root:
        return None
    if root.val==value:
        return root
    return find(root.left,value) if value<root.val else find(root.right,value)

def reuturnAncestors(root,value):
	if not root:
		return []
	if root.val == value:
		return []
	return reuturnAncestors(root.left,value) + [root.val] if value<root.val else [root.val] + reuturnAncestors(root.right,value)


m = reuturnAncestors(x,2)
