"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        while queue:
            nextQueue = deque([])
            ans.append([node.val for node in queue])
            while queue:
                node = queue.popleft()

                for child in node.children:
                    nextQueue.append(child)
                    
            queue = nextQueue
        return ans


