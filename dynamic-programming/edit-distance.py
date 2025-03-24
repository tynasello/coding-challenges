'''
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
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        minOps = [[math.inf for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        # minOps[i][j] = min ops needed to convert word1[:i] to word2[:j]
        # then minOps[i][j] = min of 
        # - minOps[i][j-1] (add the last char from word2 to end of word1)
        # - minOps[i-1][j] (delete last char from word1)
        # - minOps[i-1][j-1] (replace last char form word1 with last char from word2)
        for i in range(len(word1)+1):
            minOps[i][0] = i
        for j in range(len(word2)+1):
            minOps[0][j] = j

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    minOps[i][j] = minOps[i-1][j-1]
                else:
                    minOps[i][j] = min(
                        minOps[i][j-1], 
                        minOps[i-1][j], 
                        minOps[i-1][j-1]
                    ) + 1

        return minOps[len(word1)][len(word2)]

