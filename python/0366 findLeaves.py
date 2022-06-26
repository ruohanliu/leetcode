# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
            #tree #recursion #important

            solution 1: calculate height, collect all nodes and sort
            solution 2. collect leaves on the fly, store in defaultdict
            solution 3. topologicalsort
        """

        def dfs(root):
            if not root:
                return 0
            
            lh = dfs(root.left) + 1
            rh = dfs(root.right) + 1

            h = max(lh,rh)
            ans[h] += root.val,
            return h

        ans = defaultdict(list)
        dfs(root)
        return [ans[x] for x in sorted(ans.keys())]

    def findLeaves_sort(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
            #topologicalsort

            does not work for nodes with same values
        """

        def dfs(root):
            if not root:
                return

            if not root.left and not root.right:
                leaves.add(root.val)
            else:
                if root.left:
                    adjList[root.left.val] += root.val,
                    inDegree[root.val] += 1
                    dfs(root.left)
                if root.right:
                    adjList[root.right.val] += root.val,
                    inDegree[root.val] += 1
                    dfs(root.right)
            return

        leaves = set()
        adjList = defaultdict(list)
        inDegree = defaultdict(int)
        ans = []
        dfs(root)

        while leaves:
            ans.append(list(leaves))
            nextLeaves = []
            while leaves:
                leaf = leaves.pop()
                for parent in adjList[leaf]:
                    inDegree[parent] -= 1
                    if inDegree[parent] == 0:
                        nextLeaves.append(parent)
            leaves = nextLeaves

        return ans