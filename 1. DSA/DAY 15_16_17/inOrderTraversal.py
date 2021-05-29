def inorderTraversal(self, root):
      res, stack = [], []
      current = root
      while True:
         while current:
            stack.append(current)
            current = current.left
         if len(stack) == 0:
            return res
         node = stack[-1]
         stack.pop(len(stack)-1)
         if node.data != None:
            res.append(node.data)
         current = node.right
      return res

##Sol 2

return (self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)) if root else []