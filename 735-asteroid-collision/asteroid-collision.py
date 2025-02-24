class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for e in asteroids:
            if e > 0:
                s.append(e)
            else:
                while s and s[-1] > 0 and abs(e) > s[-1]:
                    s.pop()
                if not s or s[-1] < 0:
                    s.append(e)
                elif s and s[-1] == abs(e):
                    s.pop()
        return s