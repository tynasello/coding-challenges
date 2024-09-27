/*
 There is an elevator with maximum weight x, and n people with known weights who
 want to get from the ground floor to the top floor. What is the minimum number
 of rides needed if the people enter the elevator in an optimal order?

 For example, suppose that x = 10, n = 5 and the weights are as follows:

 person: 0 1 2 3 4
 weight: 2 3 3 5 6

 In this case, the minimum number of rides is 2. One optimal order is {0, 2, 3,
 1, 4}, which partitions the people into two rides: first {0, 2, 3} (total
 weight 10), and then {1, 4} (total weight 9).
*/

#include <iostream>
#include <utility>
using namespace std;

int main() {
  int x = 10;
  int n = 5;
  int weights[5] = {2, 3, 3, 5, 6};

  // Dynamic programming array storing two values:
  // 1) the minimum number of trips required,
  // 2) and the minimum weight of the last trip,
  // for a given index representing a subset of people (bit representation).
  pair<int, int> subset_mins[1 << n];
  subset_mins[0] = {1, 0}; // It takes one trip to carry no people

  for (int s = 1; s < (1 << n); ++s) { // Loop over all subsets of people
    subset_mins[s] = {n + 1, 0};       // Sensible maximum value
    for (int p = 0; p < n; p++) {      // Choose a particular person to go last
      if (s & (1 << p)) { // Ensure that the person is in the current subset
        auto mins_wo_p = subset_mins[s ^ (1 << p)];
        pair<int, int> mins_w_p = {mins_wo_p.first, mins_wo_p.second};
        if (mins_wo_p.second + weights[p] <= x) { // Add person to previous ride
          mins_w_p.second += weights[p];
        } else { // Person goes in a new empty ride
          mins_w_p.first++;
          mins_w_p.second = weights[p];
        }
        subset_mins[s] = min(subset_mins[s], mins_w_p);
      }
    }
  }

  int min_trips = subset_mins[(1 << n) - 1].first;
  cout << min_trips << endl;
}
