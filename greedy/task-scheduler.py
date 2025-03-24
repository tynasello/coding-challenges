'''
LeetCode 621. Task Scheduler

Given a characters array tasks, representing the tasks a CPU needs to do, where
each letter represents a different task. Tasks could be done in any order. Each
task is done in one unit of time. For each unit of time, the CPU could complete
either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period
between two same tasks (the same letter in the array), that is that there must
be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all
the given tasks.

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
'''

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        freq = defaultdict(int)
        for t in tasks:
            freq[t] += 1

        maxFreq = []
        for t, f in freq.items():
            heapq.heappush(maxFreq, [f*-1, t])
        
        waiting = deque()

        count = 0

        while maxFreq or waiting:
            while waiting and waiting[0][0] == count:
                _, t, f = waiting.popleft()
                heapq.heappush(maxFreq, [f*-1, t])

            if maxFreq:
                f, nextTask = heapq.heappop(maxFreq)
                f *= -1
                f -= 1
                if f > 0: 
                    waiting.append([count + n + 1, nextTask, f])

            count += 1
        
        return count
        