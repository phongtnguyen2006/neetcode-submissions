class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for token in tokens:
            if token.isdigit() or token[1:].isdigit():
                s.append(int(token))              # <-- int, not float
            elif token == '+':
                num1 = s.pop()
                num2 = s.pop()
                s.append(num2 + num1)
            elif token == '-':
                num1 = s.pop()
                num2 = s.pop()
                s.append(num2 - num1)
            elif token == '/':
                num1 = s.pop()
                num2 = s.pop()
                s.append(int(num2 / num1))        # <-- truncate NOW, not at the end
            elif token == '*':
                num1 = s.pop()
                num2 = s.pop()
                s.append(num2 * num1)

        return s[0]