from collections import deque, defaultdict
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        cycle detection + connectivity
        """

        adj = defaultdict(list)
        visited = set()

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        q = deque([(0, -1)])  # (node, parent)

        while q:
            curr, parent = q.popleft()

            if curr in visited:
                return False

            visited.add(curr)
            for neighbor in adj[curr]:
                if neighbor != parent:
                    q.append((neighbor, curr))

        return len(visited) == n