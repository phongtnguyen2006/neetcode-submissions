class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)

        for a, b in prerequisites:
            adj[a].append(b)

        # 0 = unvisited, 1 = currently in this DFS path, 2 = finished
        state = [0] * numCourses
        order = []

        for course in range(numCourses):
            if state[course] == 2:
                continue

            # True means all prerequisites have been explored.
            stack = [(course, False)]

            while stack:
                curra, finished = stack.pop()

                if finished:
                    state[curra] = 2
                    order.append(curra)
                    continue

                if state[curra] == 1:
                    return []
                if state[curra] == 2:
                    continue

                state[curra] = 1
                stack.append((curra, True))

                for currb in adj[curra]:
                    if state[currb] == 1:
                        return []
                    if state[currb] == 0:
                        stack.append((currb, False))

        return order