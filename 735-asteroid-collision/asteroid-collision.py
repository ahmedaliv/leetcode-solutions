class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for e in asteroids:
            while s and s[-1] > 0 and e <0:
                is_col = e + s[-1]
                if is_col > 0 :
                    e = 0
                elif is_col < 0:
                    s.pop()
                else:
                    s.pop()
                    e=0
            if e:
                s.append(e)
        return s