from collections import deque
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Maps original node -> cloned node
        node_dict = {node: Node(node.val)}
        q = deque([node])

        while q:
            curr = q.popleft()

            for nei in curr.neighbors:
                # 1. Only create clone and enqueue if neighbor hasn't been visited yet
                if nei not in node_dict:
                    node_dict[nei] = Node(nei.val)
                    q.append(nei)
                
                # 2. Connect the cloned neighbor to the current cloned node
                node_dict[curr].neighbors.append(node_dict[nei])

        return node_dict[node]