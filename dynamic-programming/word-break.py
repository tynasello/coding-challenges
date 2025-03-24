'''
Leetcode 139, Word Break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented 
into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        canseg = [False] * (len(s)+1)
        canseg[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if w == s[i:i+len(w)] and canseg[i+len(w)]:
                    canseg[i] = True
                    break

        return canseg[0]