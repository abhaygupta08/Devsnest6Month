# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def sameTree(x,y):
	# if both are at end point then end the verification
    if not x and not y:
        return True
     # if both are equal then go and chk for left and right subtree
    return (x and y) and (x.val==y.val) and sameTree(x.left,y.left) and sameTree(x.right,y.right)
    
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return sameTree(p,q)