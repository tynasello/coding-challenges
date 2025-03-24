'''
Leetcode 213, House Robber 2
You are a professional robber planning to rob houses along a street. Each house has a certain amount
of money stashed. All houses at this place are arranged in a circle. That means the first house is
the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it
will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount 
of money you can rob tonight without alerting the police.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])
        
        if n == 3:
            return max(nums[0], nums[1], nums[2])

        maxMoney1 = [0] * (n - 1) # maxMoney1[i] = max money robbed from house 0 to i (w/o house n-1)
        maxMoneyN = [0] * (n - 1) # maxMoneyN[i] = max money robbed from house 1 to i

        maxMoney1[0] = nums[0]
        maxMoney1[1] = max(nums[0], nums[1]) 

        maxMoneyN[0] = nums[1]
        maxMoneyN[1] = max(nums[1], nums[2]) 

        for i in range(2, len(nums)-1):
            maxMoney1[i] = max(nums[i] + maxMoney1[i-2], maxMoney1[i-1])
            maxMoneyN[i] = max(nums[i+1] + maxMoneyN[i-2], maxMoneyN[i-1])
        
        return max(maxMoney1[n-2], maxMoneyN[n-2])
