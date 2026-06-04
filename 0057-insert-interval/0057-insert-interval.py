class Solution(object):
    def insert(self, intervals, newInterval):
        arr = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            arr.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0],newInterval[0])
            newInterval[1] = max(intervals[i][1],newInterval[1])
            i += 1
        arr.append((newInterval[0],newInterval[1]))
        while i < len(intervals):
            arr.append(intervals[i])
            i += 1
        return arr

        