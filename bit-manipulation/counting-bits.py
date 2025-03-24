'''
Leetcode 338 Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.
'''

class Solution:
    # O(n)
    def countBits(self, n: int) -> List[int]:
        count = [0] * (n + 1)
        count[0] = 0
        if n >= 1: count[1] = 1

        for i in range(2, n+1):
            l = i >> 1
            r = i & 1
            count[i] = count[l] + r
            
        return count

    # O(nlogn)
    # def countBits(self, n: int) -> List[int]:
    #     count = [0] * (n + 1)
    #     for i in range(n+1):
    #         n = i
    #         while n > 0:
    #             if n & 1: count[i] += 1
    #             n >>= 1
        
    #     return count