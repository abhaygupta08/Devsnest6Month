# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def maxDepthoo(root):
    if not root:
        return 0
    ld = maxDepthoo(root.left)
    rd = maxDepthoo(root.right)
    depth = max(ld,rd) + 1
    return depth
            
        
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return maxDepthoo(root)
        