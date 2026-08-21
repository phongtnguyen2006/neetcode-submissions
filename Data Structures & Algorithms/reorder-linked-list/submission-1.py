# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        fast and slow ptr. find middle. reverse 2nd half then merge

        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        while prev.next:
            print(head.val, prev.val)
            nxt = head.next
            pnxt = prev.next
            head.next = prev
            prev.next = nxt
            prev = pnxt
            head = nxt


        return None