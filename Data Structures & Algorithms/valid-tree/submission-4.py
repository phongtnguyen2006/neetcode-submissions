from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        cycle detection
        """

        adj = defaultdict(list)
        visited = set()

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        q = deque([0])

        while q:
            curr = q.popleft()
            
            if curr in visited:
                return False
        
            visited.add(curr)
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    q.append(neighbor)
        
        return len(visited) == n