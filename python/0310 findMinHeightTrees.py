from typing import List
from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
            #graph #tree #longestpath #diameter #important
            Same as finding the diameter of n-ary tree.
            For the tree-alike graph, the number of centroids is no more than 2
            steps:
                1. find one endpoint of the longest path using bfs/dfs
                2. use bfs to find another endpoint

            general longestpath problem is np-hard. in DAG, it is same as finding shortest path
        """

        adjList = {v:set() for v in range(n)}
        for a,b in edges:
            adjList[a].add(b)
            adjList[b].add(a)
        
        def dfs(v,d,mid=True):
            nonlocal ans,maxLen,word
            if perm[v]:
                return
            perm[v] = True
            d+=1
            ans.append(v)
            if d > maxLen:
                maxLen = d
                if not mid:
                    word = [v]
                else:
                    if d % 2:
                        word = ans[d//2:d//2+1]
                    else:
                        word = ans[d//2-1:d//2+1]

            for _v in adjList[v]:
                dfs(_v,d,mid)
            ans.pop()
            
        word = []

        ans = []
        maxLen = 0
        perm = [False] * n
        dfs(0,0,False)

        ans = []
        maxLen = 0
        perm = [False] * n
        dfs(word[0],0,True)

        return word

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
            #topologicalsort
            edge case: edges is empty
        """
        adjList = defaultdict(set)
        for a,b in edges:
            adjList[a].add(b)
            adjList[b].add(a)

        leaves = [v for v in adjList.keys() if len(adjList[v]) == 1]
        while len(adjList)>2:
            nextLeaves = []
            while leaves:
                leaf = leaves.pop()
                for parent in adjList[leaf]:
                    adjList[parent].discard(leaf)
                    if len(adjList[parent]) == 1:
                        nextLeaves.append(parent)
                del adjList[leaf]
            leaves = nextLeaves

        return leaves if leaves else [0]