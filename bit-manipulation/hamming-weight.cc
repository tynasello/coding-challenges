/*
 LeetCode 191
 Write a function that takes the binary representation of an unsigned integer
 and returns the number of '1' bits it has (also known as the Hamming weight).
*/

#include <cstdint>
#include <iostream>
using namespace std;

class Solution {
public:
  int hammingWeight(uint32_t n) {
    int count = 0;
    while (n) {         // stop when n is 0
      count += (n & 1); // n and 1 checks if the LSB is a 1
      n >>= 1;          // shift right
    }
    return count;
  }

  int solution2(uint32_t n) {
    /*
     An alternative solution:
     We can use the fact that when we AND a number n with (n - 1), we end up
     removing a single 1 bit from the number everytime. We can simply count the
     number of times this occurs.
     Why does this work?
     If the LSB is a 1, then 1 - 1 = 0. So n AND n-1 will be have one less one
     than n (the LSB is removed). If the LSB is not a 1, then we must borrow
     from a digit to the left when we compute n-1. This will make that bit a 0,
     and the rest (to the right) 1. The bits to the right which become one were
     originally 0 and so will not affect the AND operation. The digit we
     borrow from will be removed from n when we set n to n AND n-1.
     I think there should be an easy induction proof for this.

     This time of this solution is determined by the number of ones, which is
     faster on average than the first solution which loops through all bits from
     right to left until the last 1.
     */
    int count = 0;
    while (n) {
      n = n & (n - 1);
      ++count;
    }
    return count;
  }

  int solution3(uint32_t n) { return __builtin_popcount(n); }
};

int main() {
  Solution s;
  uint32_t n = 12903;
  cout << s.hammingWeight(n) << ", " << s.solution2(n) << ", " << s.solution3(n)
       << endl;
}
