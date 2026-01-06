class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for token in tokens:
            if token.lstrip('-').isdigit():
                s.append(int(token))
            else:
                b = s.pop()
                a = s.pop()
                if token == '+':
                    s.append(a + b)
                elif token == '-':
                    s.append(a - b)
                elif token == '*':
                    s.append(a * b)
                elif token == '/':
                    s.append(int(a / b))
        return s[-1]