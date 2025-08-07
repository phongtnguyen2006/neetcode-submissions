class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        create digit map. make letter string choose n letters

        each letter keep or skip it, when add letter pop it, 
        add back once done, if len of string = n then add to res
        """

        self.dig_map = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'

        }

        self.res = []
        self.curr = ''
        self.digits = digits

        self.backtrack(0)
        print(self.res)
        if digits:
            return self.res
        return []


    def backtrack(self, i):
        # if i == len(self.digits):
        #     return
        if len(self.curr) == len(self.digits):
            self.res.append(self.curr)
            return

        for ch in self.dig_map[self.digits[i]]:
            self.curr += ch
            print(self.curr)
            self.backtrack(i + 1)
            self.curr = self.curr[0:-1]
        


    