'''
Leetcode 128, Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''

class Solution:
    # Hash Map O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        keyToLen = defaultdict(int) # num: length of subsequence

        for num in nums:
            if not keyToLen[num]:
                keyToLen[num] = keyToLen[num-1] + 1 + keyToLen[num+1]
                keyToLen[num - keyToLen[num-1]] = keyToLen[num]
                keyToLen[num + keyToLen[num+1]] = keyToLen[num]
                maxLen = max(maxLen, keyToLen[num])
        return maxLen