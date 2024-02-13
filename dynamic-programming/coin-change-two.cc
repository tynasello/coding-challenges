/*
LeetCode 518. Coin Change II

You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of
money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution {

public:
  // O(mn) time and O(n) space where m is number of coins and n is amount
  int change(int amount, vector<int> &coins) {
    int dp[amount + 1];
    for (int &el : dp) {
      el = 0;
    }
    dp[0] = 1;

    for (auto c : coins) {
      for (int n = c; n <= amount; ++n) {
        if (n - c >= 0)
          dp[n] += dp[n - c];
      }
    }

    return dp[amount];
  }

  // O(mn) time and space where m is number of coins and n is amount
  /*
    int change(int amount, vector<int> &coins) {
    int dp[coins.size()][amount + 1];
    for (auto &row : dp) {
      for (auto &el : row) {
        el = 0;
      }
      row[0] = 1;
    }

    for (int i = 0; i < coins.size(); ++i) {
      for (int n = 1; n <= amount; ++n) {
        if (n - coins[i] >= 0)
          dp[i][n] += dp[i][n - coins[i]];
        if (i - 1 >= 0)
          dp[i][n] += dp[i - 1][n];
      }
    }

    return dp[coins.size() - 1][amount];
  }
  */
};

int main() {
  vector<int> coins = {1, 2, 5};
  Solution s;
  cout << s.change(5, coins) << endl;
}
