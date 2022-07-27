"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        """
            You are given all the nodes of an N-ary tree as an array of Node objects, where each node has a unique value. Return the root of the N-ary tree.

            O(N) space
        """
        inDegree = defaultdict(int)
        for node in tree:
            for child in node.children:
                inDegree[child.val] += 1

        for node in tree:
            if inDegree[node.val] == 0:
                return node

    def findRoot(self, tree: List['Node']) -> 'Node':
        """
            if we visit every node and its children, then the root is the only node that is visited once only.
            Given a list of numbers where some of the numbers appear twice, we are asked to find the number that appear only once.

            O(1) space
        """
        bitwise = 0
        for node in tree:
            bitwise ^= node.val
            for child in node.children:
                bitwise ^= child.val

        for node in tree:
            if node.val == bitwise:
                return node