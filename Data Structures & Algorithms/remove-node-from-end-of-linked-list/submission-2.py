class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        # Create a gap of n + 1
        for _ in range(n + 1):
            fast = fast.next

        # Move both until fast reaches the end
        while fast is not None:
            slow = slow.next
            fast = fast.next

        # slow is directly before the node we want to remove
        slow.next = slow.next.next

        return dummy.next