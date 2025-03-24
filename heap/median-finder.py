'''
Leetcode 295, find median from data stream

The median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value, and the median is the mean of the two middle values.
- For example, for arr = [2,3,4], the median is 3.
- For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:
- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data structure.
- double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
'''

class MedianFinder:

    def __init__(self):
        self.count = 0
        # if count is odd, small has one more element than big
        self.small = [] # n/2 largest elements in maxheap
        self.big = [] # n/2 smallest elements in minheap
        

    def addNum(self, num: int) -> None:
        if self.count == 0:
            self.small.append(num * -1)
        elif self.count & 1:
            if self.small[0] * -1 > num:
                heapq.heappush(self.big, heapq.heappop(self.small) * -1)
                heapq.heappush(self.small, num * -1)
            else:
                heapq.heappush(self.big, num)
        else:
            if self.small[0] * -1 > num or num < self.big[0]:
                heapq.heappush(self.small, num * -1)
            else:
                heapq.heappush(self.small, heapq.heappop(self.big) * -1)
                heapq.heappush(self.big, num)
        
        self.count += 1


    def findMedian(self) -> float:
        if self.count & 1:
            return self.small[0] * -1
        else:
            return (self.small[0] * -1 + self.big[0]) / 2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()