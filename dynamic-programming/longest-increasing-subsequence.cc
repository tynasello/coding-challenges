/*
LeetCode 300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly
increasing subsequence .

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
length is 4.
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
  int lengthOfLIS(vector<int> &nums) {
    int lis = 0;
    int dp[nums.size()];
    for (auto &el : dp) {
      el = 0;
    }
    dp[0] = 1;

    for (int i = 0; i < nums.size(); ++i) {
      int curr_lis = 1;
      for (int sum = 0; sum < i; ++sum) {
        if (nums[sum] < nums[i]) {
          curr_lis = max(curr_lis, dp[sum] + 1);
        }
      }
      dp[i] = curr_lis;
      lis = max(lis, dp[i]);
    }

    return lis;
  }
};

int main() {
  Solution s;
  vector<int> nums{6, 2, 5, 1, 7, 4, 8, 3};
  cout << s.lengthOfLIS(nums);
}
