/*
LeetCode 53. Maximum Subarray
Medium
Given an integer array nums, find the subarray with the largest sum, and return
its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
  int maxSubArray(vector<int> &nums) {
    int res = nums[0];
    int dp = nums[0];

    for (int i = 1; i < nums.size(); i++) {
      dp = max(nums[i], dp + nums[i]);
      res = max(res, dp);
    }

    return res;
  }
};

int main() {
  vector<int> arr = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
  Solution s;
  cout << s.maxSubArray(arr) << endl;
  return 0;
}
