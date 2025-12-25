class Solution:
    def flipEquiv(self, root1, root2):
        def canon(root):
            if not root:
                return ()
            left = canon(root.left)
            right = canon(root.right)
            if left > right:
                left, right = right, left
            return (root.val, left, right)

        return canon(root1) == canon(root2)
