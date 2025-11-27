class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = collections.defaultdict(list)
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            adj[b].append(a)
            in_degree[a] += 1

        queue = collections.deque([i for i in range(numCourses) if in_degree[i] == 0])
        sol = []

        while queue:
            curr = queue.popleft()
            sol.append(curr)
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return sol if len(sol) == numCourses else []
