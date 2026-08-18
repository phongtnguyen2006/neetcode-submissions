"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        sorted_intervals = sorted(intervals, key=lambda interval: interval.start)
        for i in range(1, len(sorted_intervals)):
            a, b = sorted_intervals[i - 1].start, sorted_intervals[i - 1].end
            c, d = sorted_intervals[i].start, sorted_intervals[i].end
            print(a, b, c, d)
            if b > c:
                return False

        return True