class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for cuboid in cuboids:
            cuboid.sort()  # Ensure each cuboid's dimensions are sorted (l <= w <= h)
        
        # Step 2: Sort cuboids by dimensions to ensure stacking order is valid
        cuboids.sort()  # Sorting ensures smaller dimensions come first
        
        # Step 3: Recursive function with memoization
        from functools import lru_cache
        
        @lru_cache(None)
        def dfs(index, lastIndex):
            if index == len(cuboids):
                return 0  # Base case: no more cuboids
            
            max_height = 0
            
            # Option 1: Include the current cuboid if it fits
            if lastIndex == -1 or all(cuboids[index][i] >= cuboids[lastIndex][i] for i in range(3)):
                max_height = cuboids[index][2] + dfs(index + 1, index)
            
            # Option 2: Skip the current cuboid
            max_height = max(max_height, dfs(index + 1, lastIndex))
            
            return max_height
        
        # Start recursion with no previous cuboid
        return dfs(0, -1)
