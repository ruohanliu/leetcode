"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
            #clone
        """
        if not node:
            return None
        visited = {}

        def cloneNode(old,visited):
            new = Node(old.val,[])
            visited[old.val] = new
            for neighbor in old.neighbors:
                if neighbor.val not in visited:
                    new.neighbors.append(cloneNode(neighbor,visited))
                else:
                    new.neighbors.append(visited[neighbor.val])
            return new
        
        return cloneNode(node,visited)
        
        
        