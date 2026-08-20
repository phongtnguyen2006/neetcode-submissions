class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        put s1 into list by ascii. go through s2 with a window size of s1.
        for each increment down. incremet back up when leaving. if
        """

        if len(s2) < len(s1):
            return False

        letters = [0 for x in range(26)]
        ct = 0
        need = len(set(s1))          # <-- target is distinct chars, not len(s1)

        for ch in s1:
            letters[ord(ch) - 97] += 1

        i = 0
        while i < len(s1):
            letters[ord(s2[i]) - 97] -= 1

            if letters[ord(s2[i]) - 97] == 0:
                ct += 1
            elif letters[ord(s2[i]) - 97] == -1:   # <-- went over, unbalanced
                ct -= 1
            if ct == need:                          # <-- was len(s1)
                return True
            i += 1

        while i < len(s2):
            if letters[ord(s2[i - len(s1)]) - 97] == 0:
                ct -= 1
            letters[ord(s2[i - len(s1)]) - 97] += 1
            if letters[ord(s2[i - len(s1)]) - 97] == 0:   # <-- -1 back to 0
                ct += 1

            letters[ord(s2[i]) - 97] -= 1
            if letters[ord(s2[i]) - 97] == 0:
                ct += 1
            elif letters[ord(s2[i]) - 97] == -1:          # <-- went over
                ct -= 1

            if ct == need:
                return True
            i += 1

        return False