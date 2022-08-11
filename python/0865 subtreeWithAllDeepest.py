class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        """
            #tree #dfs
        """
        def findDeepestNode(node,depth):
            nonlocal maxD,parent,deepestNodes
            if node:
                if depth>maxD:
                    maxD = depth
                    deepestNodes = {node}
                elif depth == maxD:
                    deepestNodes.add(node)

                if node.left:
                    parent[node.left] = node
                if node.right:
                    parent[node.right] = node
                findDeepestNode(node.left,depth+1)
                findDeepestNode(node.right,depth+1)
            
        maxD = 0
        parent = {}
        deepestNodes = set()
        findDeepestNode(root,0)
        while len(deepestNodes) > 1:
            deepestNodes = set([parent[node] for node in deepestNodes])
        return deepestNodes.pop()