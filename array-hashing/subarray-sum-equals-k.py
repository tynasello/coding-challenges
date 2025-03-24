'''
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of
subarrays whose sum equals to k. A subarray is a contiguous non-empty sequence
of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumCount = defaultdict(int) # sumCount[x] = number of subarrays starting at index 0 with sum of x
        sumCount[0] += 1
        currSum = 0

        numKSub = 0

        for n in nums:
            currSum += n
            need = currSum - k
            if need in sumCount:
                numKSub += sumCount[need]
            sumCount[currSum] += 1

        return numKSub