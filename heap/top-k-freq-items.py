'''
Leetcode 347, Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

class Solution:
    # O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int) # number: count
        for n in nums:
            count[n] += 1

        vals = [[] for _ in range(len(nums)+1)] # i - weight, val - array of nums with weight i
        for n, c in count.items():
            vals[c].append(n)

        res = []
        for i in range(len(nums), 0, -1):
            for num in vals[i]:
                res.append(num)
                if len(res) == k:
                    return res
                
    # Min Heap O(nlogk)
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     count = defaultdict(int) # number: count
    #     for n in nums:
    #         count[n] += 1

    #     minHeap = [] # [count, number]

    #     for n, c in count.items():
    #         if len(minHeap) < k:
    #             heapq.heappush(minHeap, [c, n])
    #         elif minHeap[0][0] < c:
    #             heapq.heappop(minHeap)
    #             heapq.heappush(minHeap, [c, n])

    #     res = []
    #     while len(minHeap) > 0:
    #         res.append(heapq.heappop(minHeap)[1])

    #     return res