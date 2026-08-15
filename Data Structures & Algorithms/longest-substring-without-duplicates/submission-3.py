class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0

        curr = set()
        l = 0
        r = 1
        m = 1
        curr.add(s[l])

        while r < len(s):
            if s[r] not in curr:
                # print(curr)
                curr.add(s[r])
                m = max(len(curr), m)
                r += 1
            else:
                curr.remove(s[l])
                l += 1
        
        return m
