from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # CHANGED: If s1 is longer, no window in s2 can fit it.
        if len(s1) > len(s2):
            return False

        ch_dict = defaultdict(int)
        same = 0
        unique_ch = len(set(s1))

        # CHANGED: s1 is always the pattern; don't swap the strings.
        shorter = s1
        longer = s2

        for ch in shorter:
            ch_dict[ch] += 1

        for i in range(len(shorter)):
            ch = longer[i]

            # CHANGED: Only check characters from s1. Looking up other
            # characters in a defaultdict creates misleading zero counts.
            if ch in ch_dict:
                # CHANGED: Moving away from zero removes one match.
                if ch_dict[ch] == 0:
                    same -= 1

                ch_dict[ch] -= 1

                # CHANGED: Reaching zero adds one match.
                if ch_dict[ch] == 0:
                    same += 1

        # CHANGED: Check only after the entire first window is built.
        if same == unique_ch:
            return True

        # CHANGED: Include the final possible window (+ 1).
        for l in range(1, len(longer) - len(shorter) + 1):
            # CHANGED: l is the NEW window's start, so l - 1 leaves.
            leaving = longer[l - 1]
            r = l + len(shorter) - 1
            entering = longer[r]

            if leaving in ch_dict:
                # CHANGED: A zero count moving away from zero loses a match.
                if ch_dict[leaving] == 0:
                    same -= 1

                ch_dict[leaving] += 1

                # CHANGED: A count reaching zero gains a match.
                if ch_dict[leaving] == 0:
                    same += 1

            if entering in ch_dict:
                # CHANGED: An extra copy moves zero to -1.
                if ch_dict[entering] == 0:
                    same -= 1

                ch_dict[entering] -= 1

                # CHANGED: Reaching zero gains a match.
                if ch_dict[entering] == 0:
                    same += 1

            if same == unique_ch:
                return True

        return False