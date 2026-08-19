class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # 1. Sort meetings chronologically by start time
        intervals.sort(key=lambda x: x.start)

        # 2. Min-heap tracks the earliest end time of occupied rooms
        room_ends = []
        heapq.heappush(room_ends, intervals[0].end)

        for i in range(1, len(intervals)):
            # If the earliest ending meeting finishes before current starts, reuse that room
            if intervals[i].start >= room_ends[0]:
                heapq.heappop(room_ends)

            # Push the new meeting's end time
            heapq.heappush(room_ends, intervals[i].end)

        return len(room_ends)