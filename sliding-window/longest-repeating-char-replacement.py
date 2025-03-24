'''
Leetcode 424, Longest Repeating Character Replacement
You are given a string s and an integer k. You can choose any character of the string and change 
it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int) # count[c] = curr count of letter c in window s[i:j+1]

        i = 0
        j = 0

        while j < len(s):
            count[s[j]]+=1
            highestCount = 0
            
            for c in count.keys():
                highestCount = max(highestCount, count[c])

            if j - i + 1 - highestCount > k:
                count[s[i]]-=1
                i+=1
                
            j+=1
        
        return j-i