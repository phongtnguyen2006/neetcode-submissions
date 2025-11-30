class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == ']':
                curr = []
                top = stack.pop()
                while top != '[':
                    curr.append(top)
                    top = stack.pop()
                curr.reverse()
                mt = int(stack.pop())
                stack.extend(curr * mt)
                i += 1
            elif s[i].isdigit():
                num = ''
                while i < len(s) and s[i].isdigit():
                    num += s[i]
                    i += 1
                stack.append(num)
            else:
                stack.append(s[i])
                i += 1

        return "".join(stack)