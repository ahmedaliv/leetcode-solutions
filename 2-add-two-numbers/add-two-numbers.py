# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = [], []

        while l1:
            n1.append(str(l1.val))
            l1 = l1.next

        while l2:
            n2.append(str(l2.val))
            l2 = l2.next

        num1 = int(''.join(n1[::-1]))
        num2 = int(''.join(n2[::-1]))
        total = str(num1 + num2)[::-1]  
        dummy = ListNode(0)
        current = dummy
        for digit in total:
            current.next = ListNode(int(digit))
            current = current.next

        return dummy.next
