from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        class_dict = defaultdict(list)
        for a, b in prerequisites:
            class_dict[a].append(b)

        visited = set()   # Global set: already confirmed safe/processed
        path = set()      # Current search path: used to detect cycles

        for i in range(numCourses):
            if i in visited:
                continue

            # Stack stores tuples: (node, is_processed)
            # is_processed=False -> first time visiting (push neighbors)
            # is_processed=True  -> backtracking (remove from current path)
            s = [(i, False)]

            while s:
                curr, processed = s.pop()

                if processed:
                    path.remove(curr)
                    visited.add(curr)
                    continue

                if curr in path:
                    return False  # Cycle detected (back-edge)
                if curr in visited:
                    continue      # Already confirmed safe

                path.add(curr)
                # Re-add to stack marked as processed for backtracking step
                s.append((curr, True))

                for n in class_dict[curr]:
                    if n in path:
                        return False
                    if n not in visited:
                        s.append((n, False))

        return True