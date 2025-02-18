class MedianFinder:

    def __init__(self):
        self.med = []
        self.size = 0

    def addNum(self, num: int) -> None:
        self.size += 1
        self.med.append(num)

    def findMedian(self) -> float:
        # if odd
        self.med.sort()
        if self.size == 1:
            return self.med[0]
        if self.size % 2 != 0:
            return self.med[self.size // 2]
        else:
            return (self.med[self.size // 2] + self.med[(self.size // 2 )-1]) / 2
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder() 
# obj.addNum(num)
# param_2 = obj.findMedian()