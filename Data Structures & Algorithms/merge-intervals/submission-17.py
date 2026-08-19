class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort()
        i = 0
        while i < (len(intervals) - 1):
            interval_1 = intervals[i]
            interval_2 = intervals[i + 1]
            if interval_1[1] >= interval_2[0]:
                intervals.pop(i)
                intervals.pop(i)
                intervals.insert(i, [min(interval_1[0], interval_2[0]), max(interval_1[1], interval_2[1])])
            else:
                i += 1

        return intervals