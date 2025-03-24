'''
Leetcode 100 Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    # BFS Solution
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pq = deque()
        qq = deque()

        pq.append(p)
        qq.append(q)

        while len(pq) and len(qq):
            pn = pq.popleft()
            qn = qq.popleft()

            if pn and qn:
                if pn.val != qn.val:
                    return False
            elif pn or qn:
                return False
            
            if pn:
                pq.append(pn.left)
                pq.append(pn.right)
            if qn:
                qq.append(qn.left)
                qq.append(qn.right)

        return len(pq) == len(qq)
    
    # DFS Solution
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     ps = [p]
    #     qs = [q]

    #     while len(ps) and len(qs):
    #         pn = ps.pop()
    #         qn = qs.pop()

    #         if pn and qn:
    #             if pn.val != qn.val:
    #                 return False
    #         elif pn or qn:
    #             return False
            
    #         if pn:
    #             ps.append(pn.left)
    #             ps.append(pn.right)
    #         if qn:
    #             qs.append(qn.left)
    #             qs.append(qn.right)
        
    #     return len(ps) == len(qs)

        