'''
Leetcode 2187, Minimum Time To Complete Trips
You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

Each bus can make multiple trips successively; that is, the next trip can start immediately after 
completing the current trip. Also, each bus operates independently; that is, the trips of one bus 
do not influence the trips of any other bus.

You are also given an integer totalTrips, which denotes the number of trips all buses should make in
total. Return the minimum time required for all buses to complete at least totalTrips trips.
'''

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l = 1
        r = min(time) * totalTrips

        while l < r:
            m = l + (r-l)//2
            trips = 0
            for t in time:
                trips += m // t
            if trips >= totalTrips:
                r = m
            else:
                l = m + 1

        return r

# class Solution:
#     def minimumTime(self, time: List[int], totalTrips: int) -> int: 
#         waiting = []
#         for t in time:
#             heapq.heappush(waiting, [t, t])

#         tripCount = 0
#         timeCount = 0

#         while waiting:
#             waitingNext = []
#             while waiting and waiting[0][0] == timeCount:
#                 _, time = heapq.heappop(waiting)
#                 tripCount += 1

#                 if tripCount == totalTrips:
#                     return timeCount
                
#                 waitingNext.append(time)

#             for time in waitingNext:
#                 heapq.heappush(waiting, [timeCount + time, time])

#             timeCount += 1