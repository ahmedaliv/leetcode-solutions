from sortedcontainers import SortedSet

class Solution:
    def cmp(self, a: List[int], b: List[int]) -> bool:
        if a[1] < b[1]:
            return True
        elif a[1] == b[1]:
            return a[0] < b[0]
        return False

    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=functools.cmp_to_key(lambda a, b: -1 if self.cmp(a, b) else 1))
        days = SortedSet()
        cnt = 0
        
        for i in range(1, 100001):
            days.add(i)
            
        for event in events:
            it = days.bisect_left(event[0])
            if it < len(days) and days[it] <= event[1]:
                days.remove(days[it])
                cnt += 1
                
        return cnt