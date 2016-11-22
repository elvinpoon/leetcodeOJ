# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        r = []
        flag = 0
        merged = None
        last_end = -1e10
        for interval in intervals:
            if newInterval.start > interval.end:
                r.append(interval)
                last_end = interval.end
                continue
            elif newInterval.start>= interval.start and newInterval.start <= interval.end:
                merged = interval
                merged.start = min(interval.start,newInterval.start)
                merged.end = max(interval.end,newInterval.end)
                continue
            if newInterval.end < interval.start:
                if merged is not None:
                    if not flag:
                        r.append(merged)
                    r.append(interval)
                    flag = 1
                else:
                    if newInterval.start > last_end:
                        if not flag:
                            r.append(newInterval)
                        r.append(interval)
                        flag = 1
            else:
                if merged is not None:
                    merged.end = max(interval.end,newInterval.end)
                else:
                    merged = interval
                    merged.start = min(interval.start,newInterval.start)
                    merged.end = max(interval.end,newInterval.end)

        if not flag:
            if merged is None:
                r.append(newInterval)
            else:
                r.append(merged)
        return r