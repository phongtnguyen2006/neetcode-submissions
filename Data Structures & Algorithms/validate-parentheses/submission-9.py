class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in "({[":
                stack.append(ch)
                continue
            if ch in ")}]":
                if len(stack) == 0: return False
                top = stack.pop()
                if (ch == ')' and top != '('):
                    return False
                if (ch == '}' and top != '{'):
                    return False
                if (ch == ']' and top != '['):
                    return False
        
        if len(stack) > 0:
            return False
        return True