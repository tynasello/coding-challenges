'''
Leetcode 133, Clone Graph
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        copy = {}
        copy[node.val] = Node(node.val)

        q = deque()
        q.append(node)

        while q:
            u = q.popleft()
            for v in u.neighbors:
                if v.val not in copy:
                    copy[v.val] = Node(v.val)
                    q.append(v)
                copy[u.val].neighbors.append(copy[v.val])
                
        return copy[node.val]
        


        