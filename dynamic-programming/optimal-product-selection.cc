/*
We are given the prices of k products over n days, and we want to buy each
product exactly once. However, we are allowed to buy at most one product in a
day. What is the minimum total price? For example, consider the following
scenario (k = 3 and n = 8):

      0 1 2 3 4 5 6 7
p_0:  6 9 5 2 8 9 1 6
p_1:  8 2 6 2 8 5 7 2
p_2:  5 3 9 7 3 5 1 4

In this scenario, the minimum total price is 5:


      0 1 2 3 4 5 6 7
p_0:  _ _ _ 2 _ _ _ _
p_1:  _ 2 _ _ _ _ _ _
p_2:  _ _ _ _ _ _ 1 _
*/

#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<vector<int>> prices = {{6, 9, 5, 2, 8, 9, 1, 6},
                                {8, 2, 6, 2, 8, 5, 7, 2},
                                {5, 3, 9, 7, 3, 5, 1, 4}};

  int n = prices.size();
  int m = prices[0].size();

  // min_price[c][r] represents minimum total price after r days for a subset with binary representation equivalent to integer c
  vector<vector<int>> min_prices = vector(1 << n, vector(m, INT_MAX)); 

  for (int coli = 0; coli < m; ++coli) {
    min_prices[0][coli] = 0;
  }
  for (int rowi = 0; rowi < n; ++rowi) {
    min_prices[1 << rowi][0] = prices[rowi][0];
  }

  for (int coli = 1; coli < (1 << n); ++coli) {
    for (int rowi = 1; rowi < m; ++rowi) {
      // represents all items being taken before this day, i.e. dont take
      min_prices[coli][rowi] = min_prices[coli][rowi - 1];

      // represents choosing to take "take" on this day
      for (int take = 0; take < n; ++take) {
        if (coli & 1 << take) { // ensure take is in the current subset
          int price_without_taken = min_prices[coli ^ (1 << take)][rowi - 1]; // remove take from subset
          if (price_without_taken != INT_MAX) {
            min_prices[coli][rowi] = min(min_prices[coli][rowi], price_without_taken + prices[take][rowi]);
          }
        }
      }
    }
  }

  int min_price = min_prices[min_prices.size() - 1][min_prices[0].size() - 1];
  cout << min_price << endl;
}
