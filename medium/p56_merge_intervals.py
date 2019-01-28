"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

"""


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)

        merged = []

        for i in intervals:
            if not merged or merged[len(merged) - 1].end < i.start:
                merged.append(i)
            elif i.end > merged[len(merged) - 1].end:
                merged[len(merged) - 1].end = i.end

        return merged

    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    
    """
