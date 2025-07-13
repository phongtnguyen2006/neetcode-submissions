class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #put each word into a set. m x n time
        from collections import defaultdict

        tracker = defaultdict(list)

        for word in strs:
            letters = [0 for _ in range(27)]
            for ch in word:
                letters[ord(ch) - 97] += 1
            
            tracker[tuple(letters)].append(word)
                

        
        return list(tracker.values())