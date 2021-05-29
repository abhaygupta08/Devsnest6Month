class TreeNode():
	def __init__(self,data=0,left=None,right=None):
		self.data = data
		self.left = left
		self.right = right
##defining a Tree
y = TreeNode(4,TreeNode(1),TreeNode(2))
x = TreeNode(4,TreeNode(7,TreeNode(1),TreeNode(2)),TreeNode(5,TreeNode(6)))
'''
			1
		3      5
	  4   6
'''
'''
            4
         7     5
       1  2  6
  

'''

'''
For level order 
append 1
1 k dono nodes(jo jo ho) lekr append krdo fir 1 ko pop krke print
fir queue k phle elem pe jaao childs daalo queue mei fir pop krdo elem ko
same for other elements of queue untill no childs present
 ''' 
'''
def preOrder(root):
	if root:
		print(root.data,end=' ')
		preOrder(root.left)
		preOrder(root.right)
def inOrder(root):
	if root:
		inOrder(root.left)
		print(root.data,end=' ')
		inOrder(root.right)
def postOrder(root):
	if root:
		inorder(root.left)
		inorder(root.right)
		print(root.data,end=' ')
def lvlOrder(root):
	q = [root]
	while len(q) > 0:
		node = q.pop(0)
		print(node.data,end=' ')
		if node.left:
			q.append(node.left)
		if node.right:
			q.append(node.right)
def leafNodes(root): ##can use any type of traversal
	if root:
		if not root.left and not root.right:
			print(root.data,end=' ')
		leafNodes(root.left)
		leafNodes(root.right)


def sizeOfTree(head):
	if not head:
		return 0
	ls = sizeOfTree(head.left)
	rs = sizeOfTree(head.right)
	size = ls+rs+1;
	return size

def sumOfElemOfTree(head):
	if not head:
		return 0
	ls = sumOfElemOfTree(head.left)
	rs = sumOfElemOfTree(head.right)
	sum = ls + rs + head.data
	return sum

def maxElemInTree(head):
	if not head:
		return -10000000000  #minimum psbl interger
	ml = maxElemInTree(head.left)
	mr = maxElemInTree(head.right)
	return max(ml,mr,head.data)

def depthOfTree(head):
	if not head:
		return 0
	ld = depthOfTree(head.left)
	rd = depthOfTree(head.right)
	depth = max(ld,rd) +1
	return depth




def getLvlOrderRet(root):
	sol = []
	if not root:
		return []
	for i in range(1,depthOfTree(root)+1):
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

def isSubtree (t1,t2):
	if (t2 == None):
		return True
	if (t1 == None):
		return False
	if (t1.data == t2.data):
		return isSubtree(t1.left, t2.left) and isSubtree(t1.right, t2.right)
	return isSubtree(t1.left, t2) or isSubtree(t1.right, t2)


##descendents of a node

def presentOrNot(root,value):
	if not root:
		return False 
	return root.data==value or presentOrNot(root.left,value) or presentOrNot(root.right,value)




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
'''
#--------------------------------------------------------------------------------------------
'''
preOrder = DATA LEFT RIGHT
inOrder = LEFT RIGHT DATA

'''
preOrder = [4,7,1,2,5,6]
inOrder = [1,7,2,4,6,5]

'''
def TREEMAKER(preOrder,inOrder):
	if len(preOrder)==1 or len(inOrder)==1:
		return None
	if len(preOrder)!=0:
		root = preOrder[0]
	inIndexRoot = inOrder.index(root)
	if inIndexRoot:
		print('LEFT',inOrder[:inIndexRoot])
		print('RIGHT',inOrder[inIndexRoot+1:])
		TREEMAKER(preOrder[1:1+len(inOrder[:inIndexRoot])],inOrder[:inIndexRoot])
		TREEMAKER(preOrder[1:1+len(inOrder[inIndexRoot+1:])],inOrder[inIndexRoot+1:])
'''
# TREEMAKER(preOrder,inOrder)

'''
            4
         7     5
       1  2  6
  

'''


def inOrderindex(val,inOrder,start,end):
	for i in range(len(inOrder)):
		if inOrder[i]==val:
			return i
	return -1
i = 0
def MakeTree(preOrder,inOrder,start,end):
	global i 
	if start>end:
		return None
	node = TreeNode(preOrder[i])
	i+=1
	if start==end:
		return node
	inOrderIndex = inOrderindex(node.data,inOrder,start,end)
	node.left = MakeTree(preOrder,inOrder,start,inOrderindex-1)
	node.right = MakeTree(preOrder,inOrder,inOrderIndex+1,end)

# def maximunNode(root,maxi):
#     if not root:
#     	return maxi
#     if root.data > maxi:
#     	maxi = root.data
#     return max(maximunNode(root.left,maxi),maximunNode(root.right,maxi))
# print(maximunNode(x,-1000000))

def miniNode(root,mini):
    if not root:
    	return mini
    if root.data < mini:
    	mini = root.data
    return min(miniNode(root.left,mini),miniNode(root.right,mini))
print(miniNode(x,1000000))

