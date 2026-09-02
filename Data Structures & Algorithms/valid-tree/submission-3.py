from collections import deque, defaultdict
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = {0}
        q = deque([0])
        while q:
            curr = q.popleft()
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)

        return len(visited) == n