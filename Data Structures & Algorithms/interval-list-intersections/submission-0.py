class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            lower = max(firstList[i][0], secondList[j][0])
            upper = min(firstList[i][1], secondList[j][1])
            print(lower, upper, firstList[i], secondList[j])
            # if firstList[i][1] >= secondList[j][0]:
            if lower <= upper:
                res.append([lower, upper])

            
            if firstList[i][0] > secondList[j][1]:
                j += 1
            elif firstList[i][1] < secondList[j][0]:
                i += 1
            elif firstList[i][1] > secondList[j][1]:
                j += 1
            elif firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
                i += 1



        return res