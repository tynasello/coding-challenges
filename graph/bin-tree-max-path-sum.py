'''
Leetcode 124, Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        
        def dfs(node): # return the max path sum from node with no splitting
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)
            maxl = max(l, 0)
            maxr = max(r, 0)

            self.res = max(self.res, maxl + maxr + node.val)
            return max(maxl + node.val, node.val + maxr)

        dfs(root)
        return self.res