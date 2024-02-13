/*
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
*/

#include <iostream>
#include <queue>
#include <set>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {

public:
  int leastInterval(vector<char> &tasks, int n) {
    unordered_map<int, int> occurenceCounts;
    priority_queue<int> taskPriority;
    for (const char task : tasks) {
      occurenceCounts[task - 'A']++;
    }
    for (const auto occurenceCount : occurenceCounts) {
      taskPriority.push(occurenceCount.second);
    }

    int count = 0;

    while (!taskPriority.empty()) {
      vector<int> executedTasksRemainingCount;
      for (int i = 0; i < n + 1; ++i) {
        if (taskPriority.empty()) {
          if (!executedTasksRemainingCount.empty()) {
            count += (n + 1 - i);
          }
          break;
        }
        int priority = taskPriority.top() - 1;
        taskPriority.pop();
        if (priority != 0) {
          executedTasksRemainingCount.emplace_back(priority);
        }
        count += 1;
      }
      for (auto task : executedTasksRemainingCount) {
        taskPriority.push(task);
      }
    }

    return count;
  }
};

int main() {
  vector<char> tasks = {'A', 'A', 'A', 'B', 'B', 'B'};
  Solution s;
  cout << s.leastInterval(tasks, 2) << endl;
}
