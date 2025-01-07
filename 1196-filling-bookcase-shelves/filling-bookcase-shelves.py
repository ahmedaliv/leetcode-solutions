class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [-1] * len(books)
        def f(i):
            if i >= len(books):
                return 0
            if dp[i] != -1:
                return dp[i]
            mx_h = 0
            t_w = 0 
            dp[i] = float('inf')
            for idx in range(i,len(books)):
                t_w += books[idx][0]
                mx_h = max(mx_h,books[idx][1])

                if t_w > shelfWidth:
                    break
                dp[i] = min(dp[i],mx_h+f(idx+1))
            return dp[i]
        return f(0)