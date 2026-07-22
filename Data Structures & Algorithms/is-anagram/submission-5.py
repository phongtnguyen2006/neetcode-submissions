class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        a = defaultdict(int)
        b = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            a[s[i]] += 1
            b[t[i]] += 1

        return a == b