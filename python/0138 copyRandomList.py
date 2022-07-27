"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
            #linkedlist
        """
        visited = {}

        def helper(node):
            nonlocal visited
            if not node:
                return None
            if node in visited:
                return visited[node]
            
            _node = Node(node.val)
            visited[node] = _node
            _node.next = helper(node.next)
            _node.random = helper(node.random)
            return _node
            
        return helper(head)
        
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
            #linkedlist
        """
        if not head:
            return None
        _head = Node(head.val)
        visited = {head:_head}
        queue = [(head,_head)]
        while queue:
            node,_node = queue.pop()
            
            if node.next:
                if node.next not in visited:
                    _node.next = Node(node.next.val)
                    visited[node.next] = _node.next
                    queue.append((node.next,_node.next))
                else:
                    _node.next = visited[node.next]
                
            if node.random:
                if node.random not in visited:
                    _node.random = Node(node.random.val)
                    visited[node.random] = _node.random
                    queue.append((node.random,_node.random))
                else:
                    _node.random = visited[node.random]
        return _head