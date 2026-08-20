class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.curr = []
        self.backtrack(s, 0, 0)
        return self.res

    def backtrack(self, s, l, r):
        # consumed the whole string — curr is a valid partition
        if l == len(s):
            self.res.append(self.curr.copy())
            return
        # ran off the end without ever cutting — dead end
        if r == len(s):
            return

        # option 1: extend the current piece past r
        self.backtrack(s, l, r + 1)

        # option 2: cut here, if s[l..r] is a palindrome
        if self.check_palindrome(s, l, r):
            self.curr.append(s[l:r + 1])
            self.backtrack(s, r + 1, r + 1)
            self.curr.pop()

    def check_palindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True