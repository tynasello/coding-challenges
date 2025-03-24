'''
Leetcode 230, Kth smallest element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest 
value (1-indexed) of all the values of the nodes in the tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inOrder = []

        def dfs(u):
            if not u:
                return

            dfs(u.left)
            inOrder.append(u.val)
            dfs(u.right)

        dfs(root)

        return inOrder[k-1]

        
            
        
