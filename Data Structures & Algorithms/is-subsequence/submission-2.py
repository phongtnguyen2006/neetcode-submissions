class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        dp = set()
        l = 0
        N = len(s)
        for ch in t:
            if l < N and ch == s[l]:
                l += 1
        return l == N
