'''
Leetcode 15, 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        count = defaultdict(int) # mapping nums to num of occurences
        for i in range(n):
            count[nums[i]] += 1

        triplets = []

        for i in range(n - 1):
            ni = nums[i]
            count[ni] -= 1
            if i > 0 and ni == nums[i-1]:
                continue
            for j in range(i + 1, n):
                nj = nums[j]
                count[nj] -= 1
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                need = 0 - ni - nj
                if count[need] > 0:
                    triplets.append([ni, nj, need])

            for k in range(i + 1, n):
                count[nums[k]] += 1


        return triplets