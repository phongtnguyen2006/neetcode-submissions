from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 1. Build the directed weighted graph
        adj = defaultdict(list)
        for (src, dst), val in zip(equations, values):
            adj[src].append((dst, val))
            adj[dst].append((src, 1.0 / val))

        # 2. DFS helper to find path product from curr to target
        def dfs(curr: str, target: str, visited: set) -> float:
            if curr == target:
                return 1.0

            visited.add(curr)

            for neighbor, weight in adj[curr]:
                if neighbor not in visited:
                    res = dfs(neighbor, target, visited)
                    if res != -1.0:
                        return weight * res

            return -1.0

        # 3. Process queries
        ans = []
        for src, dst in queries:
            if src not in adj or dst not in adj:
                ans.append(-1.0)
            elif src == dst:
                ans.append(1.0)
            else:
                ans.append(dfs(src, dst, set()))

        return ans