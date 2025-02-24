class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for e in asteroids:
            to_add = True
            while s and s[-1] > 0 and e < 0:
                if s[-1] > abs(e):
                    to_add = False
                    break
                elif s[-1] < abs(e):
                    s.pop()
                else:
                    to_add = False
                    s.pop()
                    break
            if to_add:
                s.append(e)
        return s
