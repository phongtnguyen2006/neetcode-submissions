class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_key = {'(':')', '{':'}', '[':']'}
        closing_key = {')':'(', '}':'{', ']':'['}
        for ch in s:
            if ch in opening_key:
                stack.append(ch)
                continue
            if ch in closing_key:
                if not stack or stack.pop() != closing_key[ch]:
                    return False
        
        if stack:
            return False
        return True