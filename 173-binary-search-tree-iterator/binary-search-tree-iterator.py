# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.i = -1
        self.arr = []
        self.in_order(root)
    def next(self) -> int:
        self.i +=1
        return self.arr[self.i]
        

    def hasNext(self) -> bool:
        return self.i + 1 < len(self.arr)
                    
    def in_order(self,root):
        if not root:
            return None
        self.in_order(root.left)
        self.arr.append(root.val)
        self.in_order(root.right)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()