class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        my_dict = defaultdict(list)

        for i, word in enumerate(strs):
            my_dict[''.join(sorted(word))].append(i)
        
        output = []
        for key, item in my_dict.items():
            output.append([strs[i] for i in item])

        return output