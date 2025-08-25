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
            
            s = deque([i])
            while s:
                curr = s.pop()
                
                for neighbor in adj[curr]:
                    if neighbor in visited:
                        continue
                    s.append(neighbor)
                    visited.add(neighbor)

            sol += 1

        return sol


