/*
LeetCode 53
Given an integer array nums, find the subarray with the largest sum, and return
its sum.
*/

#include <cmath>
#include <vector>
using namespace std;

class Solution {
public:
  int maxSubArray(vector<int> &nums) {
    int maxSum = nums[0];
    int currSum = 0;
    for (int i = 0; i < nums.size(); ++i) {
      currSum = max(nums[i], currSum + nums[i]);
      maxSum = max(maxSum, currSum);
    }
    return maxSum;
  }
};
