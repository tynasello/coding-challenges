/*
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of
subarrays whose sum equals to k. A subarray is a contiguous non-empty sequence
of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
*/

#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
  int subarraySum(vector<int> &nums, int k) {
    int ans = 0;
    int curr = 0;
    // number of ways to make a sum using an arbitrary subarray
    // sum      -     (sum-k)       =         k
    // ^total sum     ^sum before subarray    ^desired sum
    unordered_map<int, int> sums{};
    sums[0]++;

    for (auto n : nums) {
      curr += n;
      if (sums.find(curr - k) != sums.end()) {
        ans += sums[curr - k];
      }
      sums[curr]++;
    }

    return ans;
  }
};
