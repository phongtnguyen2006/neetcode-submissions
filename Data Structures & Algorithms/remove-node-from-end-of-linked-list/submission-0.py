# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        r, l = head, dummy
        ct_r, ct_l = 0, 0   # start counts at 0

        # 1) find length of the list using r and ct_r
        while r is not None:
            r = r.next
            ct_r += 1

        # 2) move l to the node *before* the one we want to remove
        #    number of steps = length - n = ct_r - n
        while ct_l < (ct_r - n):
            l = l.next
            ct_l += 1

        # 3) skip the target node
        l.next = l.next.next

        # 4) return the (possibly new) head
        return dummy.next
