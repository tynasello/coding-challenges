'''
Leetcode 1, Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in ind:
                ind[num].append(i)
            else:
                ind[num] = [i]

        for num in nums:
            need = target-num
            if need in ind:
                if num == need:
                    if len(ind[num]) >= 2:
                        return [ind[num][0], ind[num][1]]
                else:
                    return [ind[num][0], ind[need][0]]