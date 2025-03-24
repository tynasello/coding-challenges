'''
Leetcode 3026, Maximum Good Subarray Sum

You are given an array nums of length n and a positive integer k.

A subarray of nums is called good if the absolute difference between its first and 
last element is exactly k, in other words, the subarray nums[i..j] is good if 
|nums[i] - nums[j]| == k.

Return the maximum sum of a good subarray of nums. If there are no good subarrays, return 0.
'''

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        minSum = {} # minSum[a] = minSum from some prefix subarray in nums ending before an a (not including a)
        minSum[nums[0]] = 0

        res = -math.inf

        for i in range(len(nums)):
            n = nums[i]
            currSum += n

            if n + k in minSum:
                res = max(res, currSum - minSum[n+k])
            if n - k in minSum:
                res = max(res, currSum - minSum[n-k])

            if i > 0:
                if n in minSum:
                    minSum[n] = min(minSum[n], currSum - n) 
                else:
                    minSum[n] = currSum - n

        return res if res != -math.inf else 0
