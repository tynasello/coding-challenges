'''
LeetCode 300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly
increasing subsequence .

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
length is 4.
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1 for _ in range(len(nums))] # lis[i] = lis from nums[0:i+1] ending at (including) nums[i]
        res = 1

        for i in range(len(lis)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], lis[j] + 1)
            res = max(res, lis[i])
        
        return res