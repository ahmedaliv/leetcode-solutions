# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = self.get_len(head)
        d_head = ListNode(-1,head)
        prev = self.get_nth(d_head,size-n+1)
        prev.next = prev.next.next
        return d_head.next        

    def get_len(self,head):
        cnt = 0
        cur=head
        while cur:
            cnt+=1
            cur = cur.next
        return cnt
    def get_nth(self,head,n):
        cnt = 0
        cur = head
        while cur:
            cnt +=1
            if (cnt==n):
                return cur
            cur = cur.next
        return None
