# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def sameTree(x,y):
    if not x and not y:
        return True
    return (x and y) and (x.val==y.val) and sameTree(x.left,y.left) and sameTree(x.right,y.right)

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if (s == None):
            return False
        if (t == None):
            return True
        if sameTree(s,t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)