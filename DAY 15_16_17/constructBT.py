class TreeNode():
	def __init__(self,data=0,left=None,right=None):
		self.data = data
		self.left = left
		self.right = right
##defining a Tree
y = TreeNode(4,TreeNode(1),TreeNode(2))
x = TreeNode(4,TreeNode(7,TreeNode(1),TreeNode(2)),TreeNode(5,TreeNode(6)))

preOrder = [4,7,1,2,5,6]
inorder11 = [1,7,2,4,6,5]



def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return
        root = TreeNode(preorder[0])
        ind = inorder.index(preorder.pop(0))
        root.left = self.buildTree(preorder, inorder[0:ind])
        root.right = self.buildTree(preorder, inorder[ind + 1:])
        return root

#METHOD2
	def MaKTree(preOrder,inorder):
		if len(preorder) == 0:
    		return None

        head = TreeNode(preorder[0])
        stack = [head]
        preInd, inInd = 1, 0

        while preInd < len(preorder):
            temp = None
            node = TreeNode(preorder[preInd])
            while stack and stack[-1].val == inorder[inInd]:
                temp = stack.pop()
                inInd += 1
            if temp:
                temp.right = node
            else:
                stack[-1].left = node
            stack.append(node)
            preInd += 1

        return head

'''
            4
         7     5
       1  2  6
  

'''
