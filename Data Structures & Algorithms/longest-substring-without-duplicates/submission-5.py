class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
            
        max_size = 1
        curr = set()

        l = 0
        r = 1
        curr.add(s[l])
        
        while r < len(s):
            if s[r] not in curr:
                curr.add(s[r])
                r+= 1
                max_size = max(len(curr), max_size)
            else:
                curr.remove(s[l])
                l += 1

        return max_size