from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            newInterval = res[-1]
            if newInterval[1] >= intervals[i][0]:
                res[-1] = [newInterval[0], max(newInterval[1], intervals[i][1])]
            else:
                res.append(intervals[i])
        return res
