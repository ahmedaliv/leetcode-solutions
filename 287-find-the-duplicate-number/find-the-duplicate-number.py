class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        head = 0
        while True:
            head = nums[head]
            slow = nums[slow]
            if slow == head:
                break
        return head