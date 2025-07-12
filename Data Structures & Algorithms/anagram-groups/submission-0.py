class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        output = [[strs[0]]]

        for j in range(1, len(strs)):
            insert = False
            for i in range(len(output)):
                if sorted(strs[j]) == sorted(output[i][0]):
                    output[i].append(strs[j])
                    insert = True
                    break
            if not insert:
                output.append([strs[j]])

        return output
            
