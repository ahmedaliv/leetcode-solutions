# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stk = []
        self.add_left_most_chain(root)
    def add_left_most_chain(self,root):
        while root:
            self.stk.append(root)
            root = root.left


    def next(self) -> int:
        tp = self.stk[-1]
        self.stk.pop()
        if tp.right:
            self.add_left_most_chain(tp.right)
        return tp.val


    def hasNext(self) -> bool:
        return len(self.stk)>0

                    

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()