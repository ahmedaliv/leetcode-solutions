from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0, 1, 0)])   # (pos, speed, steps)
        visited = set([(0, 1)])

        while q:
            pos, speed, steps = q.popleft()

            # found the target!
            if pos == target:
                return steps

            # Accelerate
            new_pos, new_speed = pos + speed, speed * 2
            if 0 <= new_pos <= 2 * target and (new_pos, new_speed) not in visited:
                visited.add((new_pos, new_speed))
                q.append((new_pos, new_speed, steps + 1))

            # Reverse
            new_speed = -1 if speed > 0 else 1
            if (pos, new_speed) not in visited:
                visited.add((pos, new_speed))
                q.append((pos, new_speed, steps + 1))
