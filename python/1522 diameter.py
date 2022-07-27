"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter_tle(self, root: 'Node') -> int:
        """
            topologicalsort is costly
        """
        def dfs(root):
            if not root:
                return 
            nonlocal adjList
            for child in root.children:
                adjList[root.val].add(child.val)
                adjList[child.val].add(root.val)
                dfs(child)

        if not root.children:
            return 0
        adjList = defaultdict(set)
        dfs(root)
        ans = 0
        leaves = [v for v in adjList.keys() if len(adjList[v]) == 1]
        while len(adjList)>1:
            ans += 2
            nextLeaves = []
            while leaves:
                leaf = leaves.pop()
                for parent in adjList[leaf]:
                    adjList[parent].discard(leaf)
                    if len(adjList[parent]) == 1:
                        nextLeaves.append(parent)
                del adjList[leaf]
            leaves = nextLeaves

        return ans if adjList else ans-1

    def diameter_height(self, root: 'Node') -> int:
        """
            #tree #height #recursion #important

            recursion ending condition doesnt have to be `if not root: return`
        """
        def dfs(root):
            if not root.children:
                return 0

            nonlocal ans
            max1, max2 = 0,0
            for child in root.children:
                h = dfs(child)+1
                if h > max1:
                    max1,max2 = h,max1
                elif h > max2:
                    max2 = h
            ans = max(ans,max1+max2)
            return max1

        ans = 0
        dfs(root)
        return ans

    def diameter_height(self, root: 'Node') -> int:
        """
            #tree #depti #recursion #important

            recursion ending condition doesnt have to be `if not root: return`
        """
        def dfs(root,depth):
            if not root.children:
                return depth

            nonlocal ans
            max1, max2 = depth,0
            for child in root.children:
                d = dfs(child,depth+1)
                if d > max1:
                    max1,max2 = d,max1
                elif d > max2:
                    max2 = d
            ans = max(ans,max1+max2-2*depth)
            return max1

        ans = 0
        dfs(root,0)
        return ans