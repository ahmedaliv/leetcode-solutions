class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):
            """
            Performs standard inorder traversal:
            left -> node -> right
            and links all nodes into DLL
            """
            nonlocal first,last
            if node:
              helper(node.left)
              if last:
                # link them together (last,cur Node)
                last.right = node
                node.left = last
              else:
                # only with the first node there's no last yet
                first = node
              last = node
              helper(node.right)
          if not root:
            return None
          first,last = None, None
          helper(root)
          first.left = last
          last.right = first
          return first
              
