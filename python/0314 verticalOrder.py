from typing import List,Optional
from collections import deque,defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
            #tree #traverse #dfs

            dfs traverse use stack
        """
        if not root:
            return []
        ans = []
        cnt = 0
        nodeStack = [(root, 0, 0, cnt)]
        while nodeStack:
            node, x, y, c = nodeStack.pop()
            ans.append((x, y, c, node.val))
            if node.right:
                cnt += 1
                nodeStack.append((node.right, x+1, y+1, cnt))
            if node.left:
                cnt += 1
                nodeStack.append((node.left, x-1, y+1, cnt))
        nodes, ans = ans, []
        nodes.sort()
        vertical = [nodes[0][3]]
        x = nodes[0][0]
        for i in range(1, len(nodes)):
            if nodes[i][0] == x:
                vertical.append(nodes[i][3])
            else:
                ans.append(vertical)
                vertical = [nodes[i][3]]
                x = nodes[i][0]
        ans.append(vertical)
        return ans

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
            #tree #traverse #bfs

            bfs use queue
            vertical info is already sorted because of bfs
        """
        if not root:
            return []
        queue = deque([root,0])
        columnNode = defaultdict(list)
        while queue:
            node,x = queue.popleft()
            columnNode[x].append(node.val)
            if node.left:
                queue.append([node.left,x-1])
            if node.right:
                queue.append([node.right,x+1])
        return [columnNode[x] for x in sorted(columnNode.keys())]

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
            #tree #traverse #bfs #important

            bfs use queue
            vertical info is already sorted because of bfs
            keep track of x range to avoid sorting of x keys. The range is guaranteed to be contiuous.
        """
        if not root:
            return []
        queue = deque([(root, 0)])
        columnNode = defaultdict(list)
        minX = maxX = 0
        while queue:
            node, x = queue.popleft()
            columnNode[x].append(node.val)
            minX = min(minX,x)
            maxX = max(maxX,x)
            if node.left:
                queue.append([node.left, x-1])
            if node.right:
                queue.append([node.right, x+1])
        return [columnNode[x] for x in range(minX,maxX+1)]
