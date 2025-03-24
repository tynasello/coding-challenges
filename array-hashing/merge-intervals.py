'''
Leetcode 56, Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all
 overlapping intervals, and return an array of the non-overlapping intervals 
 that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
        
        return res