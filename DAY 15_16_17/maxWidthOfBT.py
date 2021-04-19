# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def getw(root,rootlvl,rootindex,widthmap):
    if root:
        if rootlvl not in widthmap:
            widthmap[rootlvl] = [rootindex,rootindex]
        elif rootindex < widthmap[rootlvl][0]:
            widthmap[rootlvl][0] = rootindex
        elif rootindex > widthmap[rootlvl][1]:
            widthmap[rootlvl][1] = rootindex
        getw(root.left,rootlvl+1,2*rootindex+1,widthmap)
        getw(root.right,rootlvl+1,2*rootindex+2,widthmap)
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        widthmap = {}
        getw(root,0,0,widthmap)
        return max([1+x[1]-x[0] for x in widthmap.values()])