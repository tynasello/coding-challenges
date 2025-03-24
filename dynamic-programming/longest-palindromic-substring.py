'''
Leetcode 5, Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"w
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        isPal = [[False] * len(s) for _ in range(len(s))]
        
        for i in range(len(s)):
            isPal[i][i] = True
        
        maxPalLen = 1
        maxPal = [0,0]

        for i in range(len(s) - 2, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j] and (i+1 == j or isPal[i+1][j-1]):
                    isPal[i][j] = True
                    newLen = j-i+1
                    if newLen > maxPalLen:
                        maxPalLen = newLen
                        maxPal = [i, j]

        return s[maxPal[0]: maxPal[1]+1]

