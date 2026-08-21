# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        r, l = head, dummy
        ct_r, ct_l = 0, 1


        while r != None:
            r = r.next
            ct_r += 1
        while ct_l <= (ct_r - n):
            l = l.next
            ct_l += 1
        
        l.next = l.next.next

        return dummy.next