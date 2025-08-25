from collections import defaultdict, deque
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        visited = set()
        sol = 0

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        for i in range(n):
            if i in visited:
                continue
            
            # Fix: Mark start node as visited immediately
            visited.add(i)
            s = deque([i])
            
            while s:
                curr = s.pop()
                
                for neighbor in adj[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        s.append(neighbor)

            sol += 1

        return sol