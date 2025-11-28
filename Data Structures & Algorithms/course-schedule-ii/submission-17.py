class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * (numCourses)
        sol = []

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        while q:
            curr = q.pop()
            sol.append(curr)

            for nei in adj[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return sol if len(sol) == numCourses else []