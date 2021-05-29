class Solution:
	def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
		if not root1:
			return root2
		if not root2:
			return root1
        
        return TreeNode((root1.val+root2.val),self.mergeTrees(root1.left,root2.left),self.mergeTrees(root1.right,root2.right))