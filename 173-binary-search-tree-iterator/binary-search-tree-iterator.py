# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.s = []
        self.left(root)
    def next(self) -> int:
        if self.hasNext():
            tp = self.s.pop()
            if tp.right:
                self.left(tp.right)
            return tp.val
            

    def hasNext(self) -> bool:
        return len(self.s)>0
    def left(self,root):
        while root:
            self.s.append(root)
            root = root.left

            


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()