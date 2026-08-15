class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        res = ''
        for i in range(len(s)):
            l = i
            r = i
            while l >=  0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r + 1]) > len(res):
                    res = s[l:r + 1]
                l -= 1
                r += 1
            
            l = i 
            r = i + 1
            while  l >=  0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r + 1]) > len(res):
                    res = s[l:r + 1]
                l -= 1
                r += 1

        return res