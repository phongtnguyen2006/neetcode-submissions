class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []

        for ch in s:
            if ch.isalnum():
                temp.append(ch)

        for i in range(len(temp) // 2):
            if temp[i].lower() != temp[len(temp) - i - 1].lower():
                print(temp[i].lower(), temp[len(temp) - i - 1].lower())
                return False
        
        return True
            