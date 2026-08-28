class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += "%" + str(len(s)) + "#" + s
        print (output)
        return output


    def decode(self, s: str) -> List[str]:
        list = []
        i = 0

        while i < len(s):
            if (s[i] == "#"):

                temp = ""

                for j in range(i - 1, -1, -1):
                    if s[j] == "%": break
                    if not s[j].isdigit(): break
                    temp = s[j] + temp

                print (temp)

                list.append(s[i+1:(i + int(temp) + 1)])    
                i += (int(temp) + 2)
                continue

            i += 1     

        return list