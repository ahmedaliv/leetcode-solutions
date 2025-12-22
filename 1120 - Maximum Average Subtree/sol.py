class Solution:
    # Use bottom-up DFS. Return (subtree sum, subtree count) from children,
    def maximumAverageSubtree(self, root):
        self.max_avg = float("-inf")
        
        def dfs(root):
            if not root:
                return (0,0)
            ls,lc = dfs(root.left)
            rs,rc = dfs(root.right)
            ts = root.val + ls + rs 
            tc = 1 + lc + rc
            av = ts/tc
            self.max_avg = max(self.max_avg,av)
            return (ts,tc)
        
        dfs(root)
        return self.max_avg
