class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        """
            #tree #graph
        """
        def dfs(node):
            nonlocal adjList
            if node:
                if node.left:
                    adjList[node.val].add(node.left.val)
                    adjList[node.left.val].add(node.val)
                    dfs(node.left)
                if node.right:
                    adjList[node.val].add(node.right.val)
                    adjList[node.right.val].add(node.val)
                    dfs(node.right)

        adjList = defaultdict(set)
        dfs(root)
        queue = deque([k])
        if (len(adjList[k]) == 1 and root.val != k) or len(adjList[k]) == 0:
            return k
        while queue:
            for _ in range(len(queue)):
                v = queue.popleft()
                if not adjList[v] and v != root.val:
                    return v
                for _v in adjList[v]:
                    adjList[_v].discard(v)
                    queue.append(_v)