# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def getVal(root):
    while root.left:
        root = root.left
    return root
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            temp = getVal(root.right)
            root.val = temp.val
            root.right = self.deleteNode(root.right,temp.val)
        return root
            
            