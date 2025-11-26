class MedianFinder:

    def __init__(self):
        self.nums = []


    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        n = len(self.nums)
        if  n == 1:
            return self.nums[0]
        # even length
        if n % 2 == 0:
            med = (self.nums[(n//2) - 1] + self.nums[n//2]) / 2
            return med
        else:
            med = self.nums[n//2]
            return med
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()