'''
LeetCode 53. Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return
its sum.
'''

# O(n) DP
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -math.inf
        largest = [0] * (len(nums)+1) # largest[i] = largest sum possible within subarray starting at nums[i:]
        largest[len(nums)] = 0

        for i in range(len(nums)-1, -1, -1):
            largest[i] = max(nums[i], nums[i] + largest[i+1])
            res = max(res, largest[i])
        
        return res
    
# O(n) Greedy
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         currSum = 0
#         maxSum = -math.inf

#         for n in nums:
#             if currSum < 0:
#                 currSum = 0
#             currSum += n
#             maxSum = max(maxSum, currSum)

#         return maxSum