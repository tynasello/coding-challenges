'''
76. Minimum Window Substring
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window.
 If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = defaultdict(int) # count[c] = number of times char c from t is in window s[i:j+1]
        need = defaultdict(int) # need[c] = number of each char in t that we need in window s[i:j+1]
        for c in t:
            need[c] += 1
        
        i = 0
        j = 0

        for c in t:
            if c in need:
                while count[c] < need[c]:
                    if j == len(s):
                        return ""
                    if s[j] in need:
                        count[s[j]] += 1
                    j+=1
        j-=1

        minString = [i, j]
        minStringLength = j-i+1

        while i <= j and j < len(s):
            if j-i+1 < minStringLength:
                minStringLength = j-i+1
                minString = [i, j]
            if s[i] in count:
                count[s[i]] -= 1 
                while count[s[i]] < need[s[i]]:
                    if j == len(s) - 1:
                        return s[minString[0]: minString[1]+1]
                    j+=1 
                    if s[j] in count:
                        count[s[j]] += 1
            i+=1