'''
Leetcode 3, Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        taken = set()

        i = 0
        j = 0
        
        while j < len(s):
            if s[j] not in taken:
                taken.add(s[j])
                j+=1
                longest = max(longest, j-i)
            else:
                while s[i] != s[j]:
                    taken.remove(s[i])
                    i+=1
                taken.remove(s[i])
                i+=1
        
        return longest