class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()

        if (len(s) != len(t)): return False

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1

            if t[i] not in d:
                d[t[i]] = -1
            else:
                d[t[i]] -= 1
        
        for key in d:
            if (d[key]!= 0):
                return False

        return True