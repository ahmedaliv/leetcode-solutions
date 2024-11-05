import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1 :
            first = -heapq.heappop(stones)  # max stone
            second = -heapq.heappop(stones) # second max stone
            if first != second:
                heapq.heappush(stones,-(first-second))
        return -stones[0] if stones else 0

        