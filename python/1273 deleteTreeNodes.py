class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        """
            #dfs #tree
        """
        # returns the (sum of value,# of nodes) for the tree rooted at v
        def dfs(v):
            currSum = value[v]
            currN = 1
            for _v in adjList[v]:
                stSum,stN = dfs(_v)
                currSum += stSum
                currN += stN
            if currSum == 0:
                return (0,0)
            else:
                return (currSum,currN)

        adjList = defaultdict(list)
        for i,p in enumerate(parent):
            adjList[p].append(i)
        return dfs(0)[1]