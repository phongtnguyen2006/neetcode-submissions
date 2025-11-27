from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        
        # [course, prereq] -> prereq must be taken before course (prereq -> course)
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        
        # Add all courses with 0 prerequisites to the queue
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                    
        return finish == numCourses