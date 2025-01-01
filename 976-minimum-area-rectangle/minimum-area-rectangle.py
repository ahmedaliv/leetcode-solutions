class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        ans = float('inf')
        h_t = {}
        for p in points:
            if p[0] not in h_t:
                h_t[p[0]] = set()
            h_t[p[0]].add(p[1])

        n = len(points)
        for i in range(n-1):
            p1x, p1y = points[i][0], points[i][1]
            for j in range(i+1, n):
                p2x, p2y = points[j][0], points[j][1]
                # CHECK IF HORIZONTAL OR VERTICAL LINE
                if p1x == p2x or p1y == p2y:
                    continue
                
                if p2y in h_t[p1x] and p1y in h_t[p2x]:
                    ans = min(ans, abs(p1x - p2x) * abs(p1y - p2y))
        
        return 0 if ans == float('inf') else ans
