from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        tracker = defaultdict(int)
        unqiue = set()

        for a,b in trust:
            unqiue.add(a)
            tracker[b] += 1

        for key in tracker:
            print(key)
            if tracker[key] == len(unqiue):
                return key

        return -1