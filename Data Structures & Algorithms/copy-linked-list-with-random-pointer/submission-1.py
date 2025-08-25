class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        nodes = {}
        new_head = Node(head.val)       # copy of the head
        nodes[head] = new_head
        prev = new_head
        curr = head.next

        while curr:                     # pass 1: nodes + next pointers
            copy = Node(curr.val)
            nodes[curr] = copy
            prev.next = copy            # link as we go
            prev = copy
            curr = curr.next

        for node in nodes:              # pass 2: random pointers
            if node.random:
                nodes[node].random = nodes[node.random]
            else:
                nodes[node].random = None

        return new_head