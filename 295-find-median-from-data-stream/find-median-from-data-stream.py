from heapq import heappush,heappop
class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []
        self.size = 0

    def addNum(self, num: int) -> None:
        self.size += 1
        if not self.left_heap or num <= (-self.left_heap[0]):
            heappush(self.left_heap,-num)
        else:
            heappush(self.right_heap,num)
        # maintain size property
        if len(self.left_heap) > len(self.right_heap) + 1:
            heappush(self.right_heap,-self.left_heap[0])
            heappop(self.left_heap)
        elif len(self.right_heap) > len(self.left_heap):
            heappush(self.left_heap,-self.right_heap[0])
            heappop(self.right_heap)
            

    def findMedian(self) -> float:
        # if len(self.left_heap) > len(self.right_heap):
        #     return -self.left_heap[0]
        # return (-self.left_heap[0] + self.right_heap[0]) / 2
        if self.size % 2 != 0:
            return -self.left_heap[0]
        else:
            return (-self.left_heap[0] + self.right_heap[0]) / 2
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder() 
# obj.addNum(num)
# param_2 = obj.findMedian()