/*
 Leetcode 190
 Reverse bits of a given 32 bits unsigned integer.
*/

#include <cmath>
#include <cstdint>
#include <iostream>

class Solution {
public:
  uint32_t reverseBits(uint32_t n) {
    /*
     Try drawing this solution out to see how the mask is working. It is
     effectively moving the result bits to the left (progressing towards the
     reversal) while picking up bits in n to be reversed.
    */
    uint32_t res = 0;
    for (int i = 0; i < 32; ++i) {
      res = (res << 1) | (n & 1);
      n >>= 1;
    }
    return res;
  }
};
