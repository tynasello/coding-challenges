/*
LeetCode 72. Edit Distance

Given two strings word1 and word2, return the minimum number of operations
required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character


Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

*/

#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
  int minDistance(string word1, string word2) {

    if (word1.length() == 0)
      return word2.length();
    if (word2.length() == 0)
      return word1.length();

    int dp[word1.length() + 1][word2.length() + 1];

    for (int row = 0; row <= word1.length(); ++row) {
      dp[row][0] = row;
    }
    for (int col = 0; col <= word2.length(); ++col) {
      dp[0][col] = col;
    }
    dp[0][0] = 0;

    for (int row = 1; row <= word1.length(); ++row) {
      for (int col = 1; col <= word2.length(); ++col) {
        dp[row][col] =
            // Insert, deletion, replacement
            std::min(std::min(dp[row][col - 1] + 1, dp[row - 1][col] + 1),
                     dp[row - 1][col - 1] +
                         (word1[row - 1] == word2[col - 1] ? 0 : 1));
      }
    }

    return dp[word1.length()][word2.length()];
  }
};

int main() {
  Solution s;
  cout << s.minDistance("horse", "ros") << endl;
}
