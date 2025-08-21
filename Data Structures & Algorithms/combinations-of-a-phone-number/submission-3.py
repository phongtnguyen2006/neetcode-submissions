class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {'2': 'abc', '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8': "tuv", '9':"wxyz"}
        sol = []

        if not digits:
            return []

        def dfs(curr, i):
            nonlocal digits
            nonlocal sol
            
            if i == len(digits):
                sol.append(curr)
                return

            for ch in num_dict[digits[i]]:
                dfs(curr + ch, i + 1)


        dfs('', 0)
        return sol

